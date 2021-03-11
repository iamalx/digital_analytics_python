# import urllib.request, json 
# with urllib.request.urlopen('http://talentscale.com/') as url:
#     data = json.loads(url.read().decode())
#     print(data)

# import json,urllib.request
# data = urllib.request.urlopen("https://app.agencyanalytics.com/#/225784/606187/google-search-console/top-queries/").read()
# output = json.loads(data)
# print (output)

from bs4 import BeautifulSoup
import requests
# import ablantis
import re
import urllib

# page2 =  requests.get("ablantis.html")
import codecs
f = codecs.open("reporthtml.html", 'r', 'utf-8').read()
soup = BeautifulSoup(f, 'html.parser')

# print(f)
# headless browser = selinun


# url = 'https://app.agencyanalytics.com/#/225784/528537/reports/688002/view?overlay=reportEditor'
# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# url = 'http://app.agencyanalytics.com/#/225784/528537/google-analytics/channels/all'
# url2 = 'https://app.agencyanalytics.com/#/login'
# page = requests.get(url, headers={'Authorization': 'access_token myToken'})

# == Headers route 

# headers = { 
# 'accept':'*/*',
# 'accept-encoding':'gzip, deflate, br',
# 'accept-language':'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7,la;q=0.6',
# 'cache-control':'no-cache',
# 'dnt':'1',
# 'pragma':'no-cache',
# 'referer':'https',
# 'sec-fetch-mode':'no-cors',
# 'sec-fetch-site':'cross-site',
# 'user-agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
# }

# headers = { 
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
# 'accept-encoding: gzip, deflate, br'
# 'accept-language: en-US,en;q=0.9'
# 'cache-control: max-age=0'
# 'cookie: aa_referrer=https://www.google.com/; ajs_anonymous_id=%22e55a7e6d-b3fc-4908-bf43-1ce086167188%22; _ga=GA1.2.1156556825.1594192005; _fbp=fb.1.1594192005635.299123261; hubspotutk=5fb434e00a5d695c7169ad81582b0831; __hssrc=1; ajs_user_id=225784; cf_4928_id=da6b0a19-c483-4c95-9f23-da6df5d63cde; _hjid=8f0ebd9f-23e9-43a4-b39c-008a46572687; cf_4928_cta_68721=88638; _gid=GA1.2.917548178.1605484511; __hstc=29847008.5fb434e00a5d695c7169ad81582b0831.1594192005986.1605305510816.1605484511140.193; cf_4928_person_time=1605484525016; _hjAbsoluteSessionInProgress=0; cf_4928_person_last_update=1605484525501; __hssc=29847008.3.1605484511140'
# 'if-modified-since: Fri, 13 Nov 2020 20:47:16 GMT'
# 'if-none-match: W/"5faef0d4-a29"'
# 'referer: https://app.agencyanalytics.com/'
# 'sec-fetch-dest: document'
# 'sec-fetch-mode: navigate'
# 'sec-fetch-site: same-origin'
# 'sec-fetch-user: ?1'
# 'upgrade-insecure-requests: 1'
# 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
# }


# response = requests.get(url='https://app.agencyanalytics.com/#/login', headers=headers)
# print(response.text, 'sssss')

# # == Start the session route 
# session = requests.Session()
# print(session)

# # Create the payload
# payload = {'username': '', 
#           'password': ''
#         }

# # Post the payload to the site to log in
# s = session.post("https://app.agencyanalytics.com/#/login", data=payload)
# print(s)

# Navigate to the next page and scrape the data
# s = session.get(url)
# print(s, 'GETURL')

# page = requests.get(url)
# soup = BeautifulSoup(s.text, 'html.parser')
# soup.find('img')['src']




# print(soup, '-------------')
# print(soup.find_all(id="root"))
# print(ablantis.htmll)


print('----------')

# print(stats_tag_ls)
# print('----------')

# stat_labels = soup.find_all('span', class_='label')
# stats_labels_ls = [lb.get_text() for lb in stat_labels]


# classes = [value
#             for element in soup.find_all('span', class_=['negative', 'positive'])
#             for value in element["class"]]
# print(classes)
# change = soup.find_all('span', class_=['negative', 'positive'])
# print(change)

# tags = soup.find_all( attrs={"data-metric" : "users"})
# print(tags)

# stat_container = soup.find_all(True, class_= 'stat-container')
# print(stat_container)
# print(i, value)
# if value.find('%') != -1:
#     value = value.rsplit(' ',1)[0]
# value = value.replace(' ', '_')
# stat_values[value] = stats_tag_ls[i]
# stat_values[i] = value
# print(stat_values)#     print(stats_labels_ls[i])
#     print(stats_tag_ls[i])
# print(stat_values)

stat_values = {}
month = 'December'

def get_main_cards_data(): 
    stat_tags = soup.find_all('span', class_=['stat', 'label'])
    stats_tag_ls = [pt.get_text() for pt in stat_tags]
    
    for i, value in enumerate(stats_tag_ls):
        value = "".join(value.rstrip().lstrip()) 
        value = value.replace('\n', '').replace('\r', '')
        filtered_value = ''.join(filter(str.isalpha, value))
        # print(filtered_value)
        if filtered_value == '' or filtered_value == 'K':
            stats_tag_ls[i] = value
        else:
            stats_tag_ls[i] = filtered_value
            stat_values[filtered_value] = stats_tag_ls[i-1] 

get_main_cards_data()

review_values = {}
review_ls =  [
    'yext.engagement.chart.pie.calls',
    'yext.engagement.chart.pie.clicksWebsite',
    # 'yext.reviews.table',
    'yext.reach.chart.pie.views',
    'yext.engagement.chart.pie.drivingDirections',
    'yext.reach.chart.pie.searches'
]

#Todo: 
# rating_tags2 = soup.find_all(attrs={"data-widget-key" : 'yext.overview.chart.pie.reviewBreakdown'})
# rating_tags_ls2 = [i.get_text() for i in rating_tags2]
# print(rating_tags2)

def filter_data(html_ls):
    filtered_ls = [ i.get_text().split('\n') for i in html_ls]
    for i, ls in enumerate(filtered_ls):
        for y, item in enumerate(ls):
            filtered_ls[i][y] = "".join(item.rstrip().lstrip()) 
            filtered_ls[i][y] = filtered_ls[i][y].replace('\t', '')
            filtered_ls[i][y] = filtered_ls[i][y].replace('\r', '')
    filtered_ls = [list(filter(None, i)) for i in filtered_ls]
    return filtered_ls

views_breakdown = ''

def get_google_insights_data(): 
    g_insights_tags = soup.find_all(attrs={"data-state": 'interface.campaign.local.googleMyBusiness.insights'})
    g_insigths_stats_ls = []
    # for item in g_insights_tags: 
    #     # print(item)
    #     # g_insigths_stats = item.find_all(class_=['stat', 'title'])
    #     g_insigths_stats = item.find_all(class_=['stat', 'title', 'label'])[0] 
    #     print(g_insigths_stats)
    # print('g_insigths_stats', filter_data(g_insights_tags))

    g_insigths_stats = [i.find_all(class_=['stat', 'title', 'label']) for i in g_insights_tags]
    # print('g_insigths_stats', g_insigths_stats)
    
    for i, ls in enumerate(g_insigths_stats):
        for y, item in enumerate(ls):
            item = item.get_text()
            item = "".join(item.rstrip().lstrip()) 
            item = item.replace('\n', '').replace('\r', '')
            g_insigths_stats_ls.append(item)

    review_values = {
        'Views': {'Views': g_insigths_stats_ls[5]},
        'Searches': [g_insigths_stats_ls[2]],
        'Clicks to website': [g_insigths_stats_ls[7]],
        'Driving Directions': [g_insigths_stats_ls[9]],
        'Calls': [g_insigths_stats_ls[11]],
        'avgRating': [0, g_insigths_stats_ls[12]],
        'totalReviews': [0, g_insigths_stats_ls[14]],
    } 
    return review_values

def get_review_data(): 
    reviewbreak_tags = soup.find_all(attrs={"data-widget-key": 'yext.overview.chart.pie.reviewBreakdown'})
    print(reviewbreak_tags)
    if reviewbreak_tags:
        print('reviewbreak_tags')
        reviewbreak_tags = reviewbreak_tags[0].soup.find_all('tspan')
        reviewbreak_tags_ls = [i.get_text() for i in reviewbreak_tags]
        print(reviewbreak_tags_ls)
        review_values['totalReviews'] = reviewbreak_tags_ls[0] if len(reviewbreak_tags_ls) > 0 else 0

    rating_tags = soup.find_all(attrs={"data-widget-key" : 'yext.overview.chart.gauge.averageRating'})[0].find_all('span')
    rating_tags_ls = [i.get_text() for i in rating_tags]
    review_values['avgRating'] = rating_tags_ls[1]

    # re.compile("yext*")})
    for i, value in enumerate(review_ls): 
        review_tags = soup.find_all(attrs={"data-widget-key" : value})[0].find_all('tspan')
        if len(review_tags) > 0:  
            review_tags_ls = [item.get_text() for  item in review_tags]
            # print(review_tags_ls)
            if review_tags_ls[1] == 'Views':
                review_values['Views'] = {
                    review_tags_ls[1]: review_tags_ls[0],
                    review_tags_ls[2]: review_tags_ls[4],
                    review_tags_ls[5]: review_tags_ls[7],
                    review_tags_ls[8]: review_tags_ls[10],
                    review_tags_ls[11]: review_tags_ls[13],
                }   
            else:
                review_values[review_tags_ls[1]] = review_tags_ls[0]

# get_review_data()
review_dict_new_v = {}


def get_review_new_v():
    reviewbreak_tags2 = soup.find_all(attrs={"data-state": ["interface.campaign.local.yext.reach", "interface.campaign.local.yext.engagement"] })
    # print('sss', reviewbreak_tags2)
    # reviewbreak_tags_ls2 = [i.get_text() for i in reviewbreak_tags2]

    reviewbreak_tags_ls2 = [i.get_text().split('\n') for i in reviewbreak_tags2]
    reviewbreak_tags_ls2 = [list(filter(None, i)) for i in reviewbreak_tags_ls2]
    print(reviewbreak_tags_ls2)
    for i, ls in enumerate(reviewbreak_tags_ls2):
        review_values[ls[2]] = ls[1:]
    review_values['Views'] = {
        review_values['Views'][1]: review_values['Views'][0],
        review_values['Views'][2]: review_values['Views'][4],
        review_values['Views'][5]: review_values['Views'][7],
        review_values['Views'][8]: review_values['Views'][10],
        review_values['Views'][11]: review_values['Views'][13],
    }   
    print('review_values: ', review_values)
    print('review_dict_new_v: ', review_dict_new_v)
    # print('ss', reviewbreak_tags_ls2)
    
    rating_tags = soup.find_all(attrs={"data-state" : 'interface.campaign.local.yext.overview'})
    rating_tags = filter_data(rating_tags)
    print('ss', rating_tags)
    review_values['avgRating'] = rating_tags[0]
    review_values['totalReviews'] = rating_tags[1]

    views_breakdown = f': {review_values["Views"]["Google Map"]} from Google Maps, {review_values["Views"]["Google Search"]} from Google Search, {review_values["Views"]["Yelp"]} from Yelp and {review_values["Views"]["Facebook"]} from Facebook'
   
# get_review_new_v()
review_values = get_google_insights_data()
print('review_g: ',  review_values)

top_data_dict = {}
top_data_ls = []


def get_top_data(): 
    top_data_label_tags = soup.find_all(class_='common-widgets-horizontal-bar')
    top_data_label_tags_ls2 = filter_data(top_data_label_tags)
    for i, ls in enumerate(top_data_label_tags_ls2):
        top_data_dict[ls[0]] = ls[1:]
    print('top_data_dict: ', top_data_dict)

   
    # top_data_value_tags = soup.find_all(class_='horizontal-bar-value')
    # top_data_value_tags_ls = [i.get_text() for i in top_data_value_tags]
    # print('top_data_value_tags_ls: ', top_data_value_tags_ls)

get_top_data()

calls_text = ''
def get_top_calls():
    print(top_data_dict['Callrail Top Sources'])
    calls_text = ''
    if top_data_dict['Callrail Top Sources'][0] !=  'No Calls found for your date': 
        calls_text = 'Lastly' 
        for i, item in enumerate(top_data_dict['Callrail Top Sources']):
            if i%2 == 0: 
                if (i+2) != len(top_data_dict['Callrail Top Sources']) or len(top_data_dict['Callrail Top Sources']) == 1 :
                    print('h', i)
                    calls_text = calls_text + ', '+ top_data_dict['Callrail Top Sources'][i+1] + ' call came from ' + item 
                else: 
                    print('e', i)
                    calls_text = calls_text + ' and ' + top_data_dict['Callrail Top Sources'][i+1] + ' call came from ' + item
        calls_text = calls_text + '.' 

    top_call_soures = {}
    for i, item in enumerate(top_data_dict['Callrail Top Sources']):
        if i%2 == 0: 
            top_call_soures[item] = top_data_dict['Callrail Top Sources'][i+1]
    top_data_dict['Callrail Top Sources'] =  top_call_soures

    return calls_text 

calls_text = get_top_calls()

print('stat_values: ', stat_values)
print('review_values: ', review_values)

up_sessions = ''
up_users = ''

def write_reports(): 
    print('\n')
    if 'Sessions' in stat_values:
        analytics = f'Website Analytics: For the month of {month}, there were {stat_values["Sessions"]} sessions{up_sessions}, and {stat_values["Users"]} users{up_users}, with {stat_values["NewSessions"]} of them being new sessions. In addition there were a total of {stat_values["Pageviews"]} page views with an average duration of {stat_values["AvgTimeonPage"]} minutes per page.'
        print(analytics)

    if 'Calls' in stat_values:
        calls = f'Call Tracking: There were a total {stat_values["Calls"]} calls to the office on {month}, {stat_values["Answered"]} of them were answered and, {stat_values["FirstTimeCalls"]} calls were first-time calls. {calls_text}'
        print(calls)

    if 'GoogleAdsImpressions' in stat_values and stat_values['GoogleAdsImpressions'] != '0':
        gads = f'Google Ads: There were a total of {stat_values["GoogleAdsImpressions"]} Google ads impressions. In addition, there were {stat_values["GoogleAdsClicks"]} Google Ads clicks and {stat_values["GoogleAdsConversions"]} Google Ads conversions. Finally, the average cost per click for all ads was {stat_values["GoogleAdsCPC"]}.'
        print(gads)

    if 'Impressions' in stat_values and  stat_values['Impressions'] != '0':
        social_ads = f'Facebook Ads: For Facebook Ads on {month} all of the campaigns had a total of {stat_values["Impressions"]} impressions, and {stat_values["Clicks"]} clicks. In addition the ads has an average CPC of {stat_values["AverageCPC"]} and a {stat_values["CTR"]} Click-through rate. The ad with the highest Click Through Rate was {top_data_dict["Fads Clicks"][0]} with {top_data_dict["Fads Clicks"][1]}.'
        print(social_ads)


    social = f'Social Posts: For the month of {month}, there were a total of 32 posts on all platforms. 8 Facebook posts were created this month reaching over {stat_values["FacebookReach"]} users. In addition, Twitter had 8 posts with {stat_values["TwitterFollowers"]} followers and Instagram had 8 posts with {stat_values["InstagramFollowers"]} followers.'
    print(social)

    # 'For the September newsletter, there were 205 emails opened. There were 3 visits from the newsletter and there were 23 new patients for the month. In addition, there was $7351 in revenue reported from the newsletter.'
    if 'GoogleChange' in stat_values:
        seo = f'\nSEO: For this {month}, SEO ranking increased {stat_values["GoogleChange"]} points and this month we have a total of {stat_values["Backlinks"]} Backlinks. In addition, there were {stat_values["GSCImpressions"]} Organic Impressions(Searches), {stat_values["GSCClicks"]} Organic Clicks to the site, and {stat_values["OrganicSessions"]} Organic Sessions.' 
        print(seo)
        
    if 'Searches' in review_values:
        if review_values["totalReviews"][0] != 'No Reviews found for your date':
            yesReviews = f'Lastly, there were {review_values["totalReviews"][1]} reviews this month, with an average rating of {review_values["avgRating"][1]} stars.'
        else: 
            yesReviews = ''
        reviews = f'Reviews: For {month}, there were a total of {review_values["Searches"][0]} searches and {review_values["Views"]["Views"]} views{views_breakdown}. In addition, there were {review_values["Driving Directions"][0]} driving directions, {review_values["Calls"][0]} calls, and {review_values["Clicks to website"][0]} clicks to the website. {yesReviews}'
        print(reviews)
    # 'Overall, we saw good results: more users went to the website, social posts keep getting traction, the monthly newsletter keeps getting revenue and keyword ranking continues to increase in position.' 
write_reports()

def get_PPC_data():

    if 'Impressions' in stat_values and  stat_values['Impressions'] != '0':
        print(stat_values["Clicks"])
        print(stat_values["AmountSpent"])
        print(stat_values["AverageCPC"])
        print(stat_values["CTR"])
        print(stat_values["Impressions"])
    if 'Facebook' in top_data_dict['Callrail Top Sources']:
        print(top_data_dict['Callrail Top Sources']['Facebook'])
    else: 
        print(0)
        
    if 'GoogleAdsImpressions' in stat_values and  stat_values['GoogleAdsImpressions'] != '0':
        print(stat_values["GoogleAdsClicks"])
        print(stat_values["GoogleCosts"])
        print(stat_values["GoogleAdsCPC"])
        print(stat_values["GoogleCTR"])
        print(stat_values["GoogleAdsImpressions"])
    if 'Google' in top_data_dict['Callrail Top Sources']:
        print(top_data_dict['CallrailTop Sources']['Google'])
    else: 
        print(0)

get_PPC_data()


