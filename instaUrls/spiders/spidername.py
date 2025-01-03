
# # import scrapy
# # import re


# # class SpidernameSpider(scrapy.Spider):
# #     name = "spidername"
# #     allowed_domains = ["google.com"]
# #     custom_settings = {
# #         'FEEDS': {
# #             'InstagramUrls03.csv': {
# #                 'format': 'csv',
# #                 'encoding': 'utf-8'
# #             }
# #         }
# #     }
# #     def start_requests(self):


# #         cookies = {
# #             'HSID': 'AUhY-21ivbjopAVl7',
# #             'SSID': 'AFUCMKZ2FA16u7yKW',
# #             'APISID': 'RgpFmqgXkUkoMo68/AhGRFl--fpFhuV_gL',
# #             'SAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
# #             '__Secure-1PAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
# #             '__Secure-3PAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
# #             'receive-cookie-deprecation': '1',
# #             'SID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaRrAISoyIQ4gh5kemGx614gACgYKATMSARQSFQHGX2MiDR_fbbooflRnaOs1eVAtuRoVAUF8yKqek9wrIXsJ-rDH_tfb3Cke0076',
# #             '__Secure-1PSID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaz8m4l1f3PQ59pAx3ubQ9bwACgYKAVkSARQSFQHGX2MiPdc4IqhhXWFpcl6U5aTkORoVAUF8yKodT5XXr9q0JKim4buHXUXD0076',
# #             '__Secure-3PSID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXa3bj5epofHOfdaIqD0DaJ2QACgYKAZQSARQSFQHGX2MiYre-yB17uyzPv4xHyHGsyhoVAUF8yKq4ds4A7H-hBfDmkEoSEH4_0076',
# #             'SEARCH_SAMESITE': 'CgQI2psB',
# #             'AEC': 'AVYB7cqrzwlzAhDrX8ZfM_z8lCWK8PjOV73Tr5OGnIyajw0No_OcKRPi5Q',
# #             'NID': '516=horz8gQFl_mbgbqS31c9fU_4I5sDRrxrmB1uPimzkCQ_ztK7l7Xe_lYQvso_HGfiny3fApbWLh4dF7sHoE6gxsRg2OPkB6hA8BRpNi9bw8JemkOtq3X87TF3R1c0STtv-a2YtJn9kWcjQdDtOt-s3tApxL37yzF6ojbHUtlI9TUzXhkPBnxnskGmF_gpra-7HvAlT1SDyQIUfvUKU_eyOYrRHWO5sHBkBLKI45CtQH1LwR3RqgNQ_aOyrzaUuN3Oijvu6dYSEH-JagD5YAl7NKLqdy1QJ0JyG859uLy1w-dnJ4JDoNqy3dkmSFHEL_PEWJ4HENEqD-94I_niFVoJHFpPiu0y-42flfBXCCOGMzbm',
# #             '__Secure-1PSIDTS': 'sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA',
# #             '__Secure-3PSIDTS': 'sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA',
# #             'SIDCC': 'AKEyXzWhHtDJesFe08wbz9bdeYf7WKOtXZW37efwEw9uug_yAtDnBpHA40Kupj5mNDG2ajHDFJ0',
# #             '__Secure-1PSIDCC': 'AKEyXzWkrEqc_4wzucMxIF6IosfvQHIcz_MZbkI2CfBQY-JKQIkeGDzHh34P00vLTMchLmGTZw',
# #             '__Secure-3PSIDCC': 'AKEyXzWybjgZA2nqrOLCsm08_v8bOs-uNHC327W65kevMT83u2kF41Q7zfuMMHvXWFmYAgxYIQs',
# #         }

# #         headers = {
# #             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# #             'accept-language': 'en-US,en;q=0.9',
# #             'cache-control': 'max-age=0',
# #             # 'cookie': 'HSID=AUhY-21ivbjopAVl7; SSID=AFUCMKZ2FA16u7yKW; APISID=RgpFmqgXkUkoMo68/AhGRFl--fpFhuV_gL; SAPISID=bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p; __Secure-1PAPISID=bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p; __Secure-3PAPISID=bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p; receive-cookie-deprecation=1; SID=g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaRrAISoyIQ4gh5kemGx614gACgYKATMSARQSFQHGX2MiDR_fbbooflRnaOs1eVAtuRoVAUF8yKqek9wrIXsJ-rDH_tfb3Cke0076; __Secure-1PSID=g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaz8m4l1f3PQ59pAx3ubQ9bwACgYKAVkSARQSFQHGX2MiPdc4IqhhXWFpcl6U5aTkORoVAUF8yKodT5XXr9q0JKim4buHXUXD0076; __Secure-3PSID=g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXa3bj5epofHOfdaIqD0DaJ2QACgYKAZQSARQSFQHGX2MiYre-yB17uyzPv4xHyHGsyhoVAUF8yKq4ds4A7H-hBfDmkEoSEH4_0076; SEARCH_SAMESITE=CgQI2psB; AEC=AVYB7cqrzwlzAhDrX8ZfM_z8lCWK8PjOV73Tr5OGnIyajw0No_OcKRPi5Q; NID=516=horz8gQFl_mbgbqS31c9fU_4I5sDRrxrmB1uPimzkCQ_ztK7l7Xe_lYQvso_HGfiny3fApbWLh4dF7sHoE6gxsRg2OPkB6hA8BRpNi9bw8JemkOtq3X87TF3R1c0STtv-a2YtJn9kWcjQdDtOt-s3tApxL37yzF6ojbHUtlI9TUzXhkPBnxnskGmF_gpra-7HvAlT1SDyQIUfvUKU_eyOYrRHWO5sHBkBLKI45CtQH1LwR3RqgNQ_aOyrzaUuN3Oijvu6dYSEH-JagD5YAl7NKLqdy1QJ0JyG859uLy1w-dnJ4JDoNqy3dkmSFHEL_PEWJ4HENEqD-94I_niFVoJHFpPiu0y-42flfBXCCOGMzbm; __Secure-1PSIDTS=sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA; __Secure-3PSIDTS=sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA; SIDCC=AKEyXzWhHtDJesFe08wbz9bdeYf7WKOtXZW37efwEw9uug_yAtDnBpHA40Kupj5mNDG2ajHDFJ0; __Secure-1PSIDCC=AKEyXzWkrEqc_4wzucMxIF6IosfvQHIcz_MZbkI2CfBQY-JKQIkeGDzHh34P00vLTMchLmGTZw; __Secure-3PSIDCC=AKEyXzWybjgZA2nqrOLCsm08_v8bOs-uNHC327W65kevMT83u2kF41Q7zfuMMHvXWFmYAgxYIQs',
# #             'priority': 'u=0, i',
# #             'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
# #             'sec-ch-ua-arch': '"x86"',
# #             'sec-ch-ua-bitness': '"64"',
# #             'sec-ch-ua-full-version': '"126.0.6478.185"',
# #             'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.185", "Google Chrome";v="126.0.6478.185"',
# #             'sec-ch-ua-mobile': '?0',
# #             'sec-ch-ua-model': '""',
# #             'sec-ch-ua-platform': '"Windows"',
# #             'sec-ch-ua-platform-version': '"10.0.0"',
# #             'sec-ch-ua-wow64': '?0',
# #             'sec-fetch-dest': 'document',
# #             'sec-fetch-mode': 'navigate',
# #             'sec-fetch-site': 'same-origin',
# #             'sec-fetch-user': '?1',
# #             'upgrade-insecure-requests': '1',
# #             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
# #             'x-client-data': 'CIy2yQEIpbbJAQipncoBCIz3ygEIlaHLAQic/swBCIWgzQEI7ojOAQisns4BCNmnzgEIg6zOAQivrc4BCNWvzgEI5a/OAQiJss4BCKSyzgEY9MnNARihnc4BGLuuzgEYnbHOAQ==',
# #         }



# #         for i in range(290, 00, 10):
# #             base_url = f'https://www.google.com/search?q=site:instagram.com+(intitle:%22cafe%22+%7C+intitle:%22restaurant%22+%7C+intitle:%22bar%22)+-inurl:%22/reel/%22+-inurl:%22/reels/%22+-inurl:%22/explore/%22+-inurl:%22/p/%22+-inurl:%22/tags/%22+-inurl:%22/tv/%22+-inurl:%22/stories%22+-inurl:%22?locale%3D%22&sca_esv=28d067ce084b4185&rlz=1C1SQJL_enPK1103PK1103&biw=1366&bih=607&sxsrf=ADLYWILI0hhuqmPUxBbskLy6EPWeVwor1A:1721937746008&ei=Uq-iZscVxKvFzw_f2rS4Bw&start={i}&sa=N&sstk=AagrsujMyRlyAjfrkXvCPZiTLPk-DFO7bTg0dX6jXyleUVJLznRz-vQldk-xLPcaJmEmYHGq-WNerOsboGTIAiEAPaHbqEKgD5DdqnxLsz3kvgF1wpX5RNUISdVAEZa1PpMF&ved=2ahUKEwjHhrT9_cKHAxXEVfEDHV8tDXc4ChDw0wN6BAgFEBc'
# #                         # https://www.google.com/search?q=site:instagram.com+(intitle:%22cafe%22+%7C+intitle:%22restaurant%22+%7C+intitle:%22bar%22)+-inurl:%22/reel/%22+-inurl:%22/reels/%22+-inurl:%22/explore/%22+-inurl:%22/p/%22+-inurl:%22/tags/%22+-inurl:%22/tv/%22+-inurl:%22/stories%22+-inurl:%22?locale%3D%22&sca_esv=28d067ce084b4185&rlz=1C1SQJL_enPK1103PK1103&sxsrf=ADLYWILEDK4_eow1-z-vbsCn-Ir2oAg6_w:1721919149224&ei=rWaiZoyvDbKgkPIP4sOqkAI&start=300&sa=N&sstk=AagrsuiAePS_ttVulXllhNERWq4FdWsyBm2hoMRNUb63DRefJfN-F4eaVBLCTdoKQeAt2i9OuEhFCbPOlOJ7RpTsRPogq5YwKkifxQ&ved=2ahUKEwjMueLZuMKHAxUyEEQIHeKhCiIQ8tMDegQIAhAI&biw=1366&bih=607&dpr=1
# #                         https://www.google.com/search?q=site%3Ainstagram.com+(intitle%3A%22cafe%22+%7C+intitle%3A%22restaurant%22+%7C+intitle%3A%22bar%22)+-inurl%3A%22%2Freel%2F%22+-inurl%3A%22%2Freels%2F%22+-inurl%3A%22%2Fexplore%2F%22+-inurl%3A%22%2Fp%2F%22+-inurl%3A%22%2Ftags%2F%22+-inurl%3A%22%2Ftv%2F%22+-inurl%3A%22%2Fstories%22+-inurl%3A%22%3Flocale%3D%22+Alabama&rlz=1C1SQJL_enPK1103PK1103&oq=site%3Ainstagram.com+(intitle%3A%22cafe%22+%7C+intitle%3A%22restaurant%22+%7C+intitle%3A%22bar%22)+-inurl%3A%22%2Freel%2F%22+-inurl%3A%22%2Freels%2F%22+-inurl%3A%22%2Fexplore%2F%22+-inurl%3A%22%2Fp%2F%22+-inurl%3A%22%2Ftags%2F%22+-inurl%3A%22%2Ftv%2F%22+-inurl%3A%22%2Fstories%22+-inurl%3A%22%3Flocale%3D%22+Alabama&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg60gEJNTUwNTNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        
# #             yield scrapy.Request(url=base_url,headers=headers,cookies=cookies, callback=self.parse)

# #     # def parse(self, response):
# #     #     self.company(response)

# #     def parse(self, response):

# #         urls = response.xpath('//*[@class="yuRUbf"]//a[@jsname="UWckNb"]/@href').getall()
        
# #         for url in urls:
            
# #             yield {
# #                 'Instagram URL': url
# #             }









import scrapy
import re


class SpidernameSpider(scrapy.Spider):
    name = "spidername"
    allowed_domains = ["google.com"]


    custom_settings = {
        'FEEDS': {
            'VirginiaInstagramUrls.csv': {
                'format': 'csv',
                'encoding': 'utf-8'
            }
        },
        'DOWNLOADER_MIDDLEWARES' : {'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610},
        'ZYTE_SMARTPROXY_ENABLED': True,
        'ZYTE_SMARTPROXY_APIKEY': 'a974197c3da84f18882403b3eda21f12',
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 3,
        'AUTOTHROTTLE_ENABLED': True
    }
    
    

    def start_requests(self):
        # proxies = 'https://a974197c3da84f18882403b3eda21f12:@api.zyte.com:8011'
        cookies = {
            'HSID': 'AUhY-21ivbjopAVl7',
            'SSID': 'AFUCMKZ2FA16u7yKW',
            'APISID': 'RgpFmqgXkUkoMo68/AhGRFl--fpFhuV_gL',
            'SAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
            '__Secure-1PAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
            '__Secure-3PAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
            'receive-cookie-deprecation': '1',
            'SID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaRrAISoyIQ4gh5kemGx614gACgYKATMSARQSFQHGX2MiDR_fbbooflRnaOs1eVAtuRoVAUF8yKqek9wrIXsJ-rDH_tfb3Cke0076',
            '__Secure-1PSID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaz8m4l1f3PQ59pAx3ubQ9bwACgYKAVkSARQSFQHGX2MiPdc4IqhhXWFpcl6U5aTkORoVAUF8yKodT5XXr9q0JKim4buHXUXD0076',
            '__Secure-3PSID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXa3bj5epofHOfdaIqD0DaJ2QACgYKAZQSARQSFQHGX2MiYre-yB17uyzPv4xHyHGsyhoVAUF8yKq4ds4A7H-hBfDmkEoSEH4_0076',
            'SEARCH_SAMESITE': 'CgQI2psB',
            'AEC': 'AVYB7cqrzwlzAhDrX8ZfM_z8lCWK8PjOV73Tr5OGnIyajw0No_OcKRPi5Q',
            'NID': '516=horz8gQFl_mbgbqS31c9fU_4I5sDRrxrmB1uPimzkCQ_ztK7l7Xe_lYQvso_HGfiny3fApbWLh4dF7sHoE6gxsRg2OPkB6hA8BRpNi9bw8JemkOtq3X87TF3R1c0STtv-a2YtJn9kWcjQdDtOt-s3tApxL37yzF6ojbHUtlI9TUzXhkPBnxnskGmF_gpra-7HvAlT1SDyQIUfvUKU_eyOYrRHWO5sHBkBLKI45CtQH1LwR3RqgNQ_aOyrzaUuN3Oijvu6dYSEH-JagD5YAl7NKLqdy1QJ0JyG859uLy1w-dnJ4JDoNqy3dkmSFHEL_PEWJ4HENEqD-94I_niFVoJHFpPiu0y-42flfBXCCOGMzbm',
            '__Secure-1PSIDTS': 'sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA',
            '__Secure-3PSIDTS': 'sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA',
            'SIDCC': 'AKEyXzWhHtDJesFe08wbz9bdeYf7WKOtXZW37efwEw9uug_yAtDnBpHA40Kupj5mNDG2ajHDFJ0',
            '__Secure-1PSIDCC': 'AKEyXzWkrEqc_4wzucMxIF6IosfvQHIcz_MZbkI2CfBQY-JKQIkeGDzHh34P00vLTMchLmGTZw',
            '__Secure-3PSIDCC': 'AKEyXzWybjgZA2nqrOLCsm08_v8bOs-uNHC327W65kevMT83u2kF41Q7zfuMMHvXWFmYAgxYIQs',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"126.0.6478.185"',
            'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.185", "Google Chrome";v="126.0.6478.185"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-client-data': 'CIy2yQEIpbbJAQipncoBCIz3ygEIlaHLAQic/swBCIWgzQEI7ojOAQisns4BCNmnzgEIg6zOAQivrc4BCNWvzgEI5a/OAQiJss4BCKSyzgEY9MnNARihnc4BGLuuzgEYnbHOAQ==',
        }

        for i in range(0, 310, 10):
            base_url = f'https://www.google.com/search?q=site:instagram.com+(intitle:%22cafe%22+%7C+intitle:%22estaurant%22+%7C+intitle:%22bar%22)+-inurl:%22/reel/%22+-inurl:%22/reels/%22+-inurl:%22/explore/%22+-inurl:%22/p/%22+-inurl:%22/tags/%22+-inurl:%22/tv/%22+-inurl:%22/stories%22+-inurl:%22?locale%3D%22Virginia&sca_esv=b82d5f7397a53474&rlz=1C1SQJL_enPK1103PK1103&sxsrf=ADLYWIJU7vUgTmAiJn9Aye1aE2FA2zuYlw:1722369782557&ei=9kapZrDOIeaM7NYP5NSwqAE&start={i}&sa=N&sstk=AagrsujSFqQKxbJDHx6SKt3Uu36tRjdlHWvttquxhHBnXZ-cidRtFvreKJKbsj8u_jCPV2aC2Iz9ZCp_S899IVOLoFXbL5MGw5h3Iw&ved=2ahUKEwiwob64x8-HAxVmBtsEHWQqDBUQ8tMDegQIARAU&biw=1366&bih=607&dpr=1'
            yield scrapy.Request(url=base_url, cookies=cookies, headers=headers, callback=self.parse)

    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        insta_urls = [url for url in urls if "https://www.instagram.com" in url]
        insta_urls_cleaned = [re.sub(r'\?.*', '', url) for url in insta_urls]

        for url in insta_urls_cleaned:
            yield{
                'url': url
            }





# import scrapy
# import re
# import os
# import csv


# class SpidernameSpider(scrapy.Spider):
#     name = "spidername"
#     allowed_domains = ["google.com"]
#     custom_settings = {
#         'FEEDS': {
#             'AlbamaInstagramUrlsfull.csv': {
#                 'format': 'csv',
#                 'encoding': 'utf-8'
#             }
#         },
#         'DOWNLOADER_MIDDLEWARES' : {'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610},
#         'ZYTE_SMARTPROXY_ENABLED': True,
#         'ZYTE_SMARTPROXY_APIKEY': 'a974197c3da84f18882403b3eda21f12',
#         'CONCURRENT_REQUESTS': 1,
#         'DOWNLOAD_DELAY': 3,
#         'AUTOTHROTTLE_ENABLED': True
#     }
#     def _init_(self):
#         self.all_urls = self.read_csv_as_dict('AlbamaInstagramUrls60-120.csv')

#     def start_requests(self):
#         # proxies = 'https://a974197c3da84f18882403b3eda21f12:@api.zyte.com:8011'
#         cookies = {
#             'HSID': 'AUhY-21ivbjopAVl7',
#             'SSID': 'AFUCMKZ2FA16u7yKW',
#             'APISID': 'RgpFmqgXkUkoMo68/AhGRFl--fpFhuV_gL',
#             'SAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
#             '__Secure-1PAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
#             '__Secure-3PAPISID': 'bVU-6EuHtxzjLS_l/A_IFRyDRg_FZqBV0p',
#             'receive-cookie-deprecation': '1',
#             'SID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaRrAISoyIQ4gh5kemGx614gACgYKATMSARQSFQHGX2MiDR_fbbooflRnaOs1eVAtuRoVAUF8yKqek9wrIXsJ-rDH_tfb3Cke0076',
#             '__Secure-1PSID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXaz8m4l1f3PQ59pAx3ubQ9bwACgYKAVkSARQSFQHGX2MiPdc4IqhhXWFpcl6U5aTkORoVAUF8yKodT5XXr9q0JKim4buHXUXD0076',
#             '__Secure-3PSID': 'g.a000mAgF61Wf1ATD9gHNdllGlhXyO5mNqPN6pv5mhDguXJqkNMXa3bj5epofHOfdaIqD0DaJ2QACgYKAZQSARQSFQHGX2MiYre-yB17uyzPv4xHyHGsyhoVAUF8yKq4ds4A7H-hBfDmkEoSEH4_0076',
#             'SEARCH_SAMESITE': 'CgQI2psB',
#             'AEC': 'AVYB7cqrzwlzAhDrX8ZfM_z8lCWK8PjOV73Tr5OGnIyajw0No_OcKRPi5Q',
#             'NID': '516=horz8gQFl_mbgbqS31c9fU_4I5sDRrxrmB1uPimzkCQ_ztK7l7Xe_lYQvso_HGfiny3fApbWLh4dF7sHoE6gxsRg2OPkB6hA8BRpNi9bw8JemkOtq3X87TF3R1c0STtv-a2YtJn9kWcjQdDtOt-s3tApxL37yzF6ojbHUtlI9TUzXhkPBnxnskGmF_gpra-7HvAlT1SDyQIUfvUKU_eyOYrRHWO5sHBkBLKI45CtQH1LwR3RqgNQ_aOyrzaUuN3Oijvu6dYSEH-JagD5YAl7NKLqdy1QJ0JyG859uLy1w-dnJ4JDoNqy3dkmSFHEL_PEWJ4HENEqD-94I_niFVoJHFpPiu0y-42flfBXCCOGMzbm',
#             '__Secure-1PSIDTS': 'sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA',
#             '__Secure-3PSIDTS': 'sidts-CjEB4E2dkZT5poRrGGOMBxLyy4Owsd3sIX8BsddrsBZxJD7BC1MxENE4-u5r7UCMDb0YEAA',
#             'SIDCC': 'AKEyXzWhHtDJesFe08wbz9bdeYf7WKOtXZW37efwEw9uug_yAtDnBpHA40Kupj5mNDG2ajHDFJ0',
#             '__Secure-1PSIDCC': 'AKEyXzWkrEqc_4wzucMxIF6IosfvQHIcz_MZbkI2CfBQY-JKQIkeGDzHh34P00vLTMchLmGTZw',
#             '__Secure-3PSIDCC': 'AKEyXzWybjgZA2nqrOLCsm08_v8bOs-uNHC327W65kevMT83u2kF41Q7zfuMMHvXWFmYAgxYIQs',
#         }

#         headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
#             'accept-language': 'en-US,en;q=0.9',
#             'cache-control': 'max-age=0',
#             'priority': 'u=0, i',
#             'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
#             'sec-ch-ua-arch': '"x86"',
#             'sec-ch-ua-bitness': '"64"',
#             'sec-ch-ua-full-version': '"126.0.6478.185"',
#             'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.185", "Google Chrome";v="126.0.6478.185"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-model': '""',
#             'sec-ch-ua-platform': '"Windows"',
#             'sec-ch-ua-platform-version': '"10.0.0"',
#             'sec-ch-ua-wow64': '?0',
#             'sec-fetch-dest': 'document',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-site': 'same-origin',
#             'sec-fetch-user': '?1',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
#             'x-client-data': 'CIy2yQEIpbbJAQipncoBCIz3ygEIlaHLAQic/swBCIWgzQEI7ojOAQisns4BCNmnzgEIg6zOAQivrc4BCNWvzgEI5a/OAQiJss4BCKSyzgEY9MnNARihnc4BGLuuzgEYnbHOAQ==',
#         }

#         for i in range(0, 340, 10):
#             base_url = f'https://www.google.com/search?q=site:instagram.com+(intitle:%22cafe%22+%7C+intitle:%22restaurant%22+%7C+intitle:%22bar%22)+-inurl:%22/reel/%22+-inurl:%22/reels/%22+-inurl:%22/explore/%22+-inurl:%22/p/%22+-inurl:%22/tags/%22+-inurl:%22/tv/%22+-inurl:%22/stories%22+-inurl:%22?locale%3D%22+Alabama&sca_esv=53fb4b19e0a33516&rlz=1C1SQJL_enPK1103PK1103&sxsrf=ADLYWILBOYOPscLh9bwfFYb0BdDENRLrcQ:1722021085548&ei=3fSjZq2WIdPg4-EPoMzlqAI&start={i}&sa=N&sstk=AagrsugSd0tRczSkQMy-UOD41yPTqzV6MeXHhimQPdzaIwyPLOrYHL2BMnqOAMohkoqEPJ8EoT09ARW4Ilx4mHR1_VJpweEzbDclCA&ved=2ahUKEwjt-OW4tMWHAxVT8DgGHSBmGSUQ8tMDegQICRAE&biw=1366&bih=641&dpr=1'
#             yield scrapy.Request(url=base_url, headers=headers, cookies=cookies, callback=self.parse)

#     def parse(self, response):
#         urls = response.xpath('//a/@href').extract()
#         insta_urls = [url for url in urls if "https://www.instagram.com" in url]
#         insta_urls_cleaned = [re.sub(r'\?.*', '', url) for url in insta_urls]

#         for url in insta_urls_cleaned:
#             if url not in self.all_urls:
#                 yield{
#                     'url': url
#                 }
#             else:
#                 print(f'URL already exists....:   {url}')

#     def read_csv_as_dict(self, file_path):
#         # Check if the file exists
#         if os.path.exists(file_path):
#             with open(file_path, mode='r', encoding='utf-8') as csv_file:
#                 # Read the CSV file
#                 csv_reader = csv.DictReader(csv_file)
#                 # Convert to list of dictionaries
#                 data = [row['url'] for row in csv_reader]
#                 return data
#         else:
#              []