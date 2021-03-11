from bs4 import BeautifulSoup
import requests
import re
import urllib
import codecs
# headless browser = import selinun

## set up beatiful soup 
f = codecs.open("reporthtml.html", 'r', 'utf-8').read()
soup = BeautifulSoup(f, 'html.parser')
# print(f)


print('----------')

def filter_data(html_ls):
    ## returns filtered data
 
    filtered_ls = [ item.get_text().split('\n') for item in html_ls]

    for i, ls in enumerate(filtered_ls):
        for y, item in enumerate(ls):
            filtered_ls[i][y] = "".join(item.rstrip().lstrip()) 
            filtered_ls[i][y] = filtered_ls[i][y].replace('\t', '')
            filtered_ls[i][y] = filtered_ls[i][y].replace('\r', '')

    filtered_ls = [list(filter(None, item)) for item in filtered_ls]

    return filtered_ls


stat_values = {}
month = 'December'

def get_main_cards_data(): 
    ## get main data in a lists  
    
    stat_tags = soup.find_all('span', class_=['stat', 'label'])
    stats_tag_list = [tag.get_text() for tag in stat_tags]
    
    for i, value in enumerate(stats_tag_list):
        ## filter data
        value = "".join(value.rstrip().lstrip()) 
        value = value.replace('\n', '').replace('\r', '')
        filtered_value = ''.join(filter(str.isalpha, value))
        # print(filtered_value)

        ## set stat_values
        if filtered_value == '' or filtered_value == 'K':
            stats_tag_list[i] = value
        else:
            stats_tag_list[i] = filtered_value
            stat_values[filtered_value] = stats_tag_list[i-1] 

get_main_cards_data()

#TODO: 
# rating_tags2 = soup.find_all(attrs={"data-widget-key" : 'yext.overview.chart.pie.reviewBreakdown'})
# rating_tags_ls2 = [i.get_text() for i in rating_tags2]
# print(rating_tags2)

views_breakdown = ''
review_values = {}

## attributes used to scrap data
review_ls =  [
    'yext.engagement.chart.pie.calls',
    'yext.engagement.chart.pie.clicksWebsite',
    # 'yext.reviews.table',
    'yext.reach.chart.pie.views',
    'yext.engagement.chart.pie.drivingDirections',
    'yext.reach.chart.pie.searches'
]

def get_google_insights_data(): 
    ## scrap data from GOOGLE Maps API and return a dictionary of reviews

    g_insights_tags = soup.find_all(attrs={"data-state": 'interface.campaign.local.googleMyBusiness.insights'})
    g_insigths_stats_ls = []
    g_insigths_stats = [tag.find_all(class_=['stat', 'title', 'label']) for tag in g_insights_tags]

    ## filter data
    for i, ls in enumerate(g_insigths_stats):
        for y, item in enumerate(ls):
            item = item.get_text()
            item = "".join(item.rstrip().lstrip()) 
            item = item.replace('\n', '').replace('\r', '')
            g_insigths_stats_ls.append(item)
    
    ## set all review values 
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
    ## scrap data from Yext API and set a dictionary of reviews if not using GOOGLE MAP API 
    
    reviewbreak_tags = soup.find_all(attrs={"data-widget-key": 'yext.overview.chart.pie.reviewBreakdown'})
    
    ## set totalReviews
    if reviewbreak_tags:
        reviewbreak_tags = reviewbreak_tags[0].soup.find_all('tspan')
        reviewbreak_tags_ls = [tag.get_text() for tag in reviewbreak_tags]

        review_values['totalReviews'] = reviewbreak_tags_ls[0] if len(reviewbreak_tags_ls) > 0 else 0

    ## set avgRating
    rating_tags = soup.find_all(attrs={"data-widget-key" : 'yext.overview.chart.gauge.averageRating'})[0].find_all('span')
    rating_tags_ls = [tag.get_text() for tag in rating_tags]

    review_values['avgRating'] = rating_tags_ls[1]

    # re.compile("yext*")})

    ## set Views in review_values dictionary  
    for i, value in enumerate(review_ls): 
        review_tags = soup.find_all(attrs={"data-widget-key" : value})[0].find_all('tspan')
    
        if len(review_tags) > 0:  
            review_tags_ls = [item.get_text() for  item in review_tags]
    
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
    ## scrap data from Yext API and set a dictionary of reviews if not using GOOGLE MAP API --  new Version 
    reviewbreak_tags2 = soup.find_all(attrs={"data-state": ["interface.campaign.local.yext.reach", "interface.campaign.local.yext.engagement"] })
    ## filter data 
    reviewbreak_tags_ls2 = [tag.get_text().split('\n') for tag in reviewbreak_tags2]
    reviewbreak_tags_ls2 = [list(filter(None, tag)) for tag in reviewbreak_tags_ls2]

    ## filter data
    for ls in reviewbreak_tags_ls2:
        review_values[ls[2]] = ls[1:]
    
    ## set views dictionary 
    review_values['Views'] = {
        review_values['Views'][1]: review_values['Views'][0],
        review_values['Views'][2]: review_values['Views'][4],
        review_values['Views'][5]: review_values['Views'][7],
        review_values['Views'][8]: review_values['Views'][10],
        review_values['Views'][11]: review_values['Views'][13],
    }   
    
    rating_tags = soup.find_all(attrs={"data-state" : 'interface.campaign.local.yext.overview'})
    rating_tags = filter_data(rating_tags)
    ## set review values 
    review_values['avgRating'] = rating_tags[0]
    review_values['totalReviews'] = rating_tags[1]

    views_breakdown = f': {review_values["Views"]["Google Map"]} from Google Maps, {review_values["Views"]["Google Search"]} from Google Search, {review_values["Views"]["Yelp"]} from Yelp and {review_values["Views"]["Facebook"]} from Facebook'

# get_review_new_v()
review_values = get_google_insights_data()

top_data_dict = {}
top_data_ls = []

def get_top_data(): 
    ## get data (ie. top 10 most views, clicks, searches, et/c.)
    top_data_label_tags = soup.find_all(class_='common-widgets-horizontal-bar')
    top_data_label_tags_ls2 = filter_data(top_data_label_tags)

    ## set top_data_dict dictionary 
    for ls in top_data_label_tags_ls2:
        top_data_dict[ls[0]] = ls[1:]

get_top_data() 

calls_text = ''

def get_top_calls():
    ## set top data from calls

    calls_text = ''
    
    if top_data_dict['Callrail Top Sources'][0] !=  'No Calls found for your date': 
        calls_text = 'Lastly' 

        for i, item in enumerate(top_data_dict['Callrail Top Sources']):
            if i%2 == 0: 
                if (i+2) != len(top_data_dict['Callrail Top Sources']) or len(top_data_dict['Callrail Top Sources']) == 1 :
                    calls_text = calls_text + ', '+ top_data_dict['Callrail Top Sources'][i+1] + ' call came from ' + item 
                else: 
                    calls_text = calls_text + ' and ' + top_data_dict['Callrail Top Sources'][i+1] + ' call came from ' + item
        
        calls_text = calls_text + '.' 

    top_call_soures = {}
    ## set top_data_dict dictionary 
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
    ## concatinate string of data
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
    ## print PPC data from Goog Ads and FB ads
    if 'Impressions' in stat_values and  stat_values['Impressions'] != '0':
        print(stat_values['Clicks'])
        print(stat_values['AmountSpent'])
        print(stat_values['AverageCPC'])
        print(stat_values['CTR'])
        print(stat_values['Impressions'])
    
    if 'Facebook' in top_data_dict['Callrail Top Sources']:
        print(top_data_dict['Callrail Top Sources']['Facebook'])
    else: 
        print(0)
        
    if 'GoogleAdsImpressions' in stat_values and  stat_values['GoogleAdsImpressions'] != '0':
        print(stat_values['GoogleAdsClicks'])
        print(stat_values['GoogleCosts'])
        print(stat_values['GoogleAdsCPC'])
        print(stat_values['GoogleCTR'])
        print(stat_values['GoogleAdsImpressions'])
    
    if 'Google' in top_data_dict['Callrail Top Sources']:
        print(top_data_dict['CallrailTop Sources']['Google'])
    else: 
        print(0)

get_PPC_data()


