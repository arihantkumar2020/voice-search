from .models import RecentClass, PopularClass

def getrecentsearches():

    recent_obj = RecentClass()

    recent_obj.recent_search_1 = 'coronavirus'
    recent_obj.recent_search_2 = 'django framework'
    recent_obj.recent_search_3 = 'python django'
    recent_obj.recent_search_4 = 'emilia clarke'

    return recent_obj





def getpopularsearches():

    popular_obj = PopularClass()

    popular_obj.popular_search_1 = 'data science'
    popular_obj.popular_search_2 = 'machine learning'
    popular_obj.popular_search_3 = 'artificial intelligence'
    popular_obj.popular_search_4 = 'image processing'

    return popular_obj


