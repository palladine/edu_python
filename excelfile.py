from django.core.management.base import BaseCommand
from django.http import HttpResponse
import csv
import tablib
from datetime import datetime
from django.utils import timezone
from django.db.models import Q
import xlsxwriter


from api.models import Card, Transaction


class Command(BaseCommand):

    def handle(request, *args, **options):

        # Cards
        query = Card.objects.only('pk').filter(status=1)

        workbook = xlsxwriter.Workbook('api/static/cards.xlsx')
        worksheet = workbook.add_worksheet()
        date_format = workbook.add_format({'num_format': 'dd/mm/yyyy hh:mm'})
        bold = workbook.add_format({'bold': 1})

        # title
        list_title = ['ID карты', 'ID Key', 'Банк', 'Держатель карты', 'Маскированный номер', 'Статус', 'Срок действия',
                      'Баланс', 'Валюта баланса', 'Holds', 'Дата и время обновления']
        for c in range(len(list_title)):
            worksheet.write(0, c, list_title[c], bold)

        row = 1
        col = 0

        for elem in query:
            worksheet.write(row, col, elem.card_id_bank)
            worksheet.write(row, col + 1, elem.id_key)
            worksheet.write(row, col + 2, elem.bank.name)
            worksheet.write(row, col + 3, elem.fio)
            worksheet.write(row, col + 4, elem.masked_pan)
            worksheet.write(row, col + 5, elem.status)
            worksheet.write(row, col + 6, elem.exp_date)
            worksheet.write(row, col + 7, elem.balance)
            worksheet.write(row, col + 8, elem.currency)
            worksheet.write(row, col + 9, elem.holds)
            worksheet.write(row, col + 10, elem.upd_date.replace(tzinfo=None), date_format)
            row += 1

        workbook.close()


        # Transactions
        tquery = Transaction.objects.only('pk').all()

        tworkbook = xlsxwriter.Workbook('api/static/transactions.xlsx')
        tworksheet = tworkbook.add_worksheet()
        tdate_format = tworkbook.add_format({'num_format': 'dd/mm/yyyy hh:mm'})
        tbold = tworkbook.add_format({'bold': 1})

        # title
        tlist_title = ['Дата транзакции', 'ID Key', 'Маскированный номер', 'Держатель карты', 'Номер счета', 'Банк', 'Сумма транзакции', 'Валюта',
                      'Терминал', 'Merch', 'Код категории продавца', 'DC', 'Дата и время добавления']
        for c in range(len(tlist_title)):
            tworksheet.write(0, c, tlist_title[c], tbold)

        row = 1
        col = 0

        for telem in tquery:
            idk = telem.id_key
            card = Card.objects.filter(id_key=idk)

            tworksheet.write(row, col, telem.date_tran.replace(tzinfo=None), tdate_format)
            tworksheet.write(row, col + 1, idk)
            if card.exists():
                tworksheet.write(row, col + 2, card.first().masked_pan)
                tworksheet.write(row, col + 3, card.first().fio)
            else:
                tworksheet.write(row, col + 2, '-')
                tworksheet.write(row, col + 3, '-')
            tworksheet.write(row, col + 4, telem.card_account)
            tworksheet.write(row, col + 5, telem.bank.name)
            tworksheet.write(row, col + 6, telem.sum_tran)
            tworksheet.write(row, col + 7, telem.cur)
            tworksheet.write(row, col + 8, telem.device)
            tworksheet.write(row, col + 9, telem.merch)
            tworksheet.write(row, col + 10, telem.mcc)
            tworksheet.write(row, col + 11, telem.dc)
            tworksheet.write(row, col + 12, telem.add_date.replace(tzinfo=None), tdate_format)
            row += 1

        tworkbook.close()