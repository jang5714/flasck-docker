from lecture import contacts
from lecture.scraping.music import Music


def main():
    mr = Music()
    while 1:
        menu = contacts.menu(['exit', 'bug (URL),Melon (URL)', 'output', 'print dict', 'dict to dataframe', 'df to csv'])
        if menu == 0:
            break
        elif menu == 1:
            site = int(input('1-벅스 2-멜론'))
            if site == 1:
                mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
                mr.query_string = 'chartdate=20210720&charthour=16'
                mr.class_name.append('artist')
                mr.class_name.append('title')
                mr.tag_name = 'p'
                mr.set_html()
            else:
                mr.domain = 'https://www.melon.com/chart/index.htm?'
                mr.query_string = 'dayTime=2021072107'
                mr.class_name.append('ellipsis rank02')
                mr.class_name.append('ellipsis rank01')
                mr.tag_name = 'div'
                mr.set_html()
        elif menu == 2:
                mr.get_raking()
        elif menu == 3:
            mr.insert_dict()
        elif menu == 4:
            mr.dict_to_dataframe()
        elif menu == 5:
            mr.fname = 'text'
            mr.df_to_csv()