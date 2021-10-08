import time
import requests
import json
import sys
import ctypes
from datetime import datetime
from colorama import Fore

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("Token Informtions - Made by SP")
    tokeninfo()
    print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } You can find: \n\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Username           {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } User ID                   {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Creation Date             {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Avatar URL\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token              {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Nitro Status              {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Expiration date           {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Phone Number\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Email              {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } 2FA/MFA Enabled           {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Flags                     {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Language\n""")
    print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Email Verified     {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Payment Method            {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Payment Type\n\n\n""")
    global token
    print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Enter the token on which you want to find information : """)
    token = str(input(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token: """))

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
    }

    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }

    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)

    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        
        language = languages.get(locale)
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        billing_info = []

        for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
            y = x['billing_address']
            name = y['name']
            address_1 = y['line_1']
            address_2 = y['line_2']
            city = y['city']
            postal_code = y['postal_code']
            state = y['state']
            country = y['country']

            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                
                data = {
                    'Payment Type': 'Credit Card',
                    'Valid': not x['invalid'],
                    'CC Holder Name': name,
                    'CC Brand': cc_brand.title(),
                    'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            elif x['type'] == 2:
                data = {
                    'Payment Type': 'PayPal',
                    'Valid': not x['invalid'],
                    'PayPal Name': name,
                    'PayPal Email': x['email'],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            billing_info.append(data)

        print(f"""\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Basic Information:""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Username: {user_name}""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } User ID: {user_id}""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Creation Date: {creation_date}""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Avatar URL: {avatar_url if avatar_id else ""}""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Token: {token}\n\n""")
        
        print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Nitro Information:""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Nitro Status: {has_nitro}""")

        if has_nitro:
            print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Expires in: {days_left} day(s)\n\n""")
        else:
            print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Expires in: None day(s)\n\n""")

        print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Contact Information:""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Phone Number: {phone_number if phone_number else ""}""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Email: {email if email else ""}\n\n""")

        if len(billing_info) > 0:
            print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Billing Information:""")
            if len(billing_info) == 1:
                for x in billing_info:
                    for key, val in x.items():
                        if not val:
                            continue
                        print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))

            else:
                for i, x in enumerate(billing_info):
                    title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                    print('    ' + title)
                    print('    ' + ('=' * len(title)))
                    for j, (key, val) in enumerate(x.items()):
                        if not val or j == 0:
                            continue
                        print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))

                    if i < len(billing_info) - 1:
                        print('\n')

            print('\n')

        print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Account Security:""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } 2FA/MFA Enabled: {mfa_enabled}""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Flags: {flags}\n\n""")
        print(f"""{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Other:""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Locale: {locale} ({language})""")
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTWHITE_EX }+{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Email Verified: {verified}""")

    elif res.status_code == 401:
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Invalid token""")
        time.sleep(2)
        exit(0)

    else:
        print(f"""          {Fore.LIGHTYELLOW_EX }[{Fore.LIGHTRED_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } An error occurred while sending request""")
        time.sleep(2)
        exit(0)
    
    input(f"""\n\n\n{Fore.LIGHTYELLOW_EX }[{Fore.LIGHTBLUE_EX }#{Fore.LIGHTYELLOW_EX }]{Fore.LIGHTWHITE_EX } Press ENTER to exit""")
    exit(0)

main()