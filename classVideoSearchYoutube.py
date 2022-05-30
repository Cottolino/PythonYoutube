from youtubesearchpython import VideosSearch
# from youtubesearchpython import *

from youtubesearchpython import Comments

n_iter = 0
n_iter_succ = 20
counter = 0


class SingleSearch:
    def __init__(self, str, lim) -> None:
        self.videosSearch = VideosSearch(str, lim)
        self.Result = []
        self.Punteggio = []
        self.hours = []
        for result in self.videosSearch.result()['result']:
            self.Result.append(result)
    
    def asd(self):
        self.Result[0] = self.Result[1]

    def ordina(self):
        lunghezza = self.get_len()

        for i in range(0,lunghezza-1):
            index = i
            for j in range(i+1, lunghezza):
                # if(self.Result[j]['viewCount']['text'] < self.Result[index]['viewCount']['text']):
                if(self.get_view(j) > self.get_view(index)):
                    
                    index = j
            tmp = self.Result[index]
            self.Result[index] = self.Result[i]
            self.Result[i] = tmp

#     for (int i=0; i<arr.length-1; i++) {
#       int index = i;
#       for (int j=i+1; j<arr.length; j++)
#          if (arr[j] < arr[index]) 
#             index = j;
      
#       int temp = arr[index];  
#       arr[index] = arr[i];
#       arr[i] = temp;
#    }

    def stampa_links(self) -> None:
        # print(type(self.Result))
        # print(self.Result)
        for x in self.Result:
            print(x['link'])
    
    def stampa_views(self) -> None:
        for x in self.Result:
            print(x['viewCount']['short'])

    def get_view(self, index) -> int:
        if (self.Result[index]['viewCount']['text'] is None):
            return 0
        if("views" in self.Result[index]['viewCount']['text']):
            tmp = self.Result[index]['viewCount']['text'].replace('views','').replace(',','')
            n = float(tmp)
        return n

    def get_result(self, index) -> None:
        return self.Result[index]

    def punteggio_views(self) -> int:
        tmp = 0
        for x in self.Result:
            if(x['viewCount']['short'] is None):
                tmp2 = 0
            elif('K views' in x['viewCount']['short']):
                str1 = x['viewCount']['short'].replace('K views','')
                tmp2 = float(str1) * 1000
            elif('M views' in x['viewCount']['short']):
                str1 = x['viewCount']['short'].replace('M views','')
                tmp2 = float(str1) * 1000000
            elif('views' in x['viewCount']['short']):
                str1 = x['viewCount']['short'].replace('views','')
                tmp2 = float(str1)
            else:
                str1 = x['viewCount']['short']
                tmp2 = float(str1)
            
            tmp = tmp2
            self.Punteggio.append(tmp)
        return self.Punteggio

    def punteggio_view(self, index ,nlike):
        # if ('K views' in self.Result[index]['viewCount']['short']):
        #     str1 = self.Result[index]['viewCount']['short'].replace('K views','')
        #     tmp3 = float(str1) * 1000
        # else:
        #     str1 = self.Result[index]['viewCount']['short']
        #     tmp3 = float(str1)
        view = self.get_view(index)
        print(f'Viste: {view} Like {nlike}')
        return view + nlike
        

    def stampa_punteggi(self):
        index = 0
        for x in self.Result:
            print(x['link'])
            print(self.Punteggio[index])
            index += 1
        
    def get_len(self):
        return len(self.Result)

    def data_time(self):
        for x in self.Result:
            if('hours ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('hours ago', '')
                ore = int(str1)
            elif('hour ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('hour ago', '')
                ore = int(str1)
            elif('minutes ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('minutes ago', '')
                ore = int(str1) / 60
            elif('minute ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('minute ago', '')
                ore = int(str1) / 60
                
            
                
            # print(f'Ore {str1}')
            elif('months ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('months ago', '')
                ore = int(str1) * 744
            elif('month ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('month ago', '')
                ore = int(str1) * 744
            elif('weeks ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('weeks ago', '')
                ore = int(str1) * 168
            elif('week ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('week ago', '')
                ore = int(str1) * 168
            elif('days ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('days ago', '')
                ore = int(str1) * 24
            elif('day ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('day ago', '')
                ore = int(str1) * 24
                
            elif('years ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('years ago', '')
                ore = int(str1) * 8928
            elif('year ago' in x['publishedTime']):
                str1 = x['publishedTime'].replace('year ago', '')
                ore = int(str1) * 8928
            else:
                str1 = x['publishedTime']
                ore = int(str1)

            # self.hours.append(int(str1))
            self.hours.append(ore)
            

    def stampa_ora(self):
        print(self.hours)

    def stampa_ore_short(self):
        for x in self.Result:
            print(x['publishedTime'])


class Comments2:
    # def __init__(self, str, lim) -> None:
    #     self.post = SingleSearch(str, lim)
    #     self.num_commenti = 0
    
    def __init__(self, obj) -> None:
        self.post = obj
        self.num_commenti = 0


    def stampa(self) -> None:
        print(type(self.comment['id']))
        print(self.comment['id'])
        
        print(type(self.comments2))
        print(self.comments2)

    def get_num_like(self, index):

        nlike = 0
        self.comment = self.post.get_result(index)

        # print(comment)
        # self.comments2 = Comments(self.comment['id'])
        # print(self.comment['id'])
        # if (iter(self.comments2.comments)):
        #     if not(self.comments2 is None):
                # print(len(self.comments2.comments))
                # while self.comments2.hasMoreComments:
                    # print(len(self.comments2.comments))
                    # counter = 0
                # for x in self.comments2.comments['result']:
                    # print(x['votes']['simpleText'])
                #     if(x['votes']['simpleText'] is None):
                #         tmp = tmp + 0
                #     elif('K' in x['votes']['simpleText']):
                #         str1 = x['votes']['simpleText'].replace('K','')
                #         tmp = float(str1) * 1000
                #     else:
                #         tmp = float(x['votes']['simpleText'])
                #     nlike += tmp
                # counter += 1
                # self.comments2.getNextComments()
        # print(counter)
        # self.comments2.clear()
        
        self.comments2 = Comments.get(self.comment['id'])
        # print(self.comment['id'])
        if not(self.comments2['result'] is None):
            global n_iter
            global n_iter_succ
            global counter

            newArray = self.comments2['result'][n_iter : n_iter_succ]
            # n_iter = n_iter + 20
            # n_iter_succ = n_iter_succ + 20

            if (iter(self.comments2)):
                if not(self.comments2 is None):

                    nlike = 0
                    tmp = 0
                    # n_iter = n_iter + 1
                    for x in newArray:
                        if(x['votes']['simpleText'] is None):
                                tmp = 0
                        elif('K' in x['votes']['simpleText']):
                            str1 = x['votes']['simpleText'].replace('K','')
                            tmp = float(str1) * 1000
                        else:
                            tmp = float(x['votes']['simpleText'])
                        nlike += tmp
                        counter += 1
                    # print(counter)
                    # print(f'n_iter:{n_iter} n_iter_succ:{n_iter_succ} counter:{counter}')
                    
                    
                    n_iter = counter
                    n_iter_succ = counter + 20
                    

        # self.num_commenti = nlike
        # print(self.num_commenti)
                return nlike

        



