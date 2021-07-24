import requests


GatherLINK = input('tiktok video link > ')

url = "https://www.tiktok.com/api/share/settings/?aid=1988&app_name=tiktok_web&device_platform=webapp_pc&device_id=6987530745909036549&region=DK&priority_region=&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=da-DK&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F92.0.4515.107+Safari%2F537.36&browser_online=true&verifyFp=verify_krfa96cw_p2Eae0I8_dJaE_4XwS_AEGm_KOmG1m49cOwX&app_language=en&timezone_name=Europe%2FCopenhagen&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=5&battery_info=1"

payload={}
headers = {
  'authority': 'www.tiktok.com',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'accept': 'application/json, text/plain, */*',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': GatherLINK,#'https://www.tiktok.com/@girlscantcode/video/6971163064779558149?is_copy_url=1&is_from_webapp=v1',
  'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'tt_webid_v2=6987530745909036549; tt_webid=6987530745909036549; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22version%22:%22v2%22}; s_v_web_id=verify_krfa96cw_p2Eae0I8_dJaE_4XwS_AEGm_KOmG1m49cOwX; MONITOR_WEB_ID=6987530745909036549; tt_csrf_token=ePCjBjwO15QhaDbSrq7NMj6L; R6kq3TV7=AGIivtV6AQAAN-OR-sxIv18EYkOMaPvth3F_97xkhJ_OT_yI7nG6UayUCYRk|1|0|d52a182c37413d8803c7100633cc49d673b8b993; csrf_session_id=d3b7880ce8d34ce0821782de56fae639; ttwid=1%7C0D_adjNZXWbKipMeZG_RUyaNe6bFDSttsAX927MCOZ8%7C1627085269%7Ca8c435fe7c0aa935dcdcab5bb320b799be31cc449a11494df5ee6686cf7b8989'
}

response = requests.request("GET", url, headers=headers, data=payload)
while True:
  print(response.text)
