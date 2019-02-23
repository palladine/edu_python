class GetFileAccruals(View):
    def get(self, request):

        # request to api core
        url = models.Settings.objects.first().api_url

        headers = {}    # headers

        bs = models.Roles.objects.get(user=self.request.user).bonus_system.pk

        data = {"version": "latest",
                "method": "getaccruals",
                "bank": "all",
                "scope": [],
                "args": {"bank": "" , "bs": bs}
                }

        try:
            response_api = requests.post(url, json=data, headers=headers)
            accruals = response_api.json().get('result').get('accruals')

            general_list = []
            for accrual in accruals:
                card_abs = accrual.get('card_abs')
                card = accrual.get('card')
                fio = accrual.get('fio')
                account = accrual.get('account')
                total_user = accrual.get('total_user')
                total_operator = accrual.get('total_operator')
                total_system = accrual.get('total_system')
                currency = accrual.get('currency')
                accrual_list = [card_abs, card, fio, account, total_user, total_operator, total_system, currency]
                general_list.append(accrual_list)

            # form and save file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="accruals.csv"'

            csvwriter = csv.writer(response, delimiter=';')
            titles = ['АБС ID', 'ID', 'Держатель', 'Счет', 'Сумма начисления', 'Сумма начисления оператору',
                      'Сумма начисления системе', 'Валюта']
            csvwriter.writerow(titles)

            for rec in general_list:
                csvwriter.writerow(rec)

            return response

        except Exception as err:
            context = {'error': err}
            return render(request, 'partner_side/extends/cash_register.html', context=context)


    def post(self):
        pass