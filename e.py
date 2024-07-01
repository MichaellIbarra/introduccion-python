import requests

url = "https://site.q10.com/Conversaciones/Sync/Conversaciones"
params = {
    "lastSync": "05-22-2024 07:51",
    "persona": "119914622097"
}

headers = {
    "accept": "*/*",
    "accept-language": "es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-PE;q=0.4,es-MX;q=0.3",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://site.q10.com/",
    "referrerPolicy": "strict-origin-when-cross-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}

cookies = {
    "twk_uuid_58cd5967ab48ef44ecdbe068": "%7B%22uuid%22%3A%221.1UilbK4SeJuXkshDTs7z7giVOUzRCJ1nKcHUyhPhGzy0RZfbNYh0rHXAIg3FnuGcdqhMGL1wpdUthHUUjeG6kUEY7DgD18Oc5Tdt9PJzMnw58gc%22%2C%22version%22%3A3%2C%22domain%22%3A%22q10.com%22%2C%22ts%22%3A1709615667821%7D; _ga=GA1.2.1996084261.1716495225; _ga_B73T8V2V13=GS1.2.1716495225.1.0.1716495225.0.0.0; .ASPXANONYMOUS=3N9v5WcZJfLURPdaEM0OYzb9uBCu1-GOmsZG3QNqnDTAOIzOUncjkWV0DorFEpsDaRCPeSES0CNh1g3eFpDspAAES16A-t3V1By4ApaxQesrNkXmGT6hFdhWeXJC6cS_zE326Q2; XperiCode.CacheTempData.SessionId=48b7c289-1378-4342-a968-516af42ad33e; ARRAffinity=3baabe8ad23304a395ab7db2ad0c0ce1e04e2b96c9c7b096056e08c27627630a; ARRAffinitySameSite=3baabe8ad23304a395ab7db2ad0c0ce1e04e2b96c9c7b096056e08c27627630a; .AspNet.ApplicationCookie=v0fZSkEmD769aDOKqNQuNuAqvaRKh_W86Jv4ESeAAtBLse5tZHjNt6oS739sHVGDqD-9IUHBNAB9v3QYj_6gxqygwLLunqDUZ8hEQ88g3PM2msVn0sK_WoBzMvhSK9qvsAmooCyO_SHdZ6NNZq0B3ZtyjypleTax_Pm-D5pkYLOJ8Uxk-txdjUKHkJQIMR8-K7eD-DPjx52jv-G1bEiwZ_tRnUMrvl29gKRE6AB2ntoNqOQTeK5a6XpBLk7knPaFHTQkLS4e0X0bKZOoX4o44QuOuSXbkuOPo-UOG7OvSjo__d96fcl4RnNgwhzcwP7pQCoDCn6TgCleKRxB1bciStism-kvCSmHeqbKHFhnAGKblxB_ub26Urn2z3Fv9RipA7N2-rbl8UKQnqA-OMEZTOpAB4X3V0Y81ZJZzRZ4A8oiJWbE6xt902qlORLsev95azn3nWjdZ63s54Zd13fN5hI87Ko0vXHwNKsCoK9r98p2SeFnes9Bv3mmHAYOOY32aFhwAPnOUpwKpAJe8ADMxv37vxQ"
}

response = requests.get(url, params=params, headers=headers, cookies=cookies)

print("Código de estado:", response.status_code)
print("Contenido de la respuesta:", response.text)
