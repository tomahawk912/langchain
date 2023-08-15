import os
import requests


def scrape_linkedin_profile(_config_info, linkedin_profile_url: str, check=0):
    if check == 1:
        # My Profile 출력 (Github Gist 등록파일) : Proxcurl API 호출비용 절감을 위해
        response = requests.get(
            "https://gist.githubusercontent.com/tomahawk912/8cd8a32f074ea4c4050033f1f1e2ed5e/raw/e1eef23220f5038827ea9e99f68ecbc5aa6f304c/tomahawk912.json"
        )
        # print(gist_response.json()['full_name'])
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {
            "Authorization": f'Bearer {_config_info.get("PROXYCURL_API_KEY")}'
        }

        response = requests.get(
            api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewd", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


# if __name__ == "__main__":
#     linkedin_data = scrape_linkedin_profile(
#         linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/"
#     )
#     print(linkedin_data.json())
