from django.shortcuts import render, HttpResponse, redirect
from movieApp import models
import pymysql


# Create your views here.


def index(request):
    return render(request, "index.html")


def getMovie(request):
    datalist = []
    title = request.GET.get("title", None)
    if title is not None:
        conn = pymysql.connect(db="movies", unix_socket='/cloudsql/ca675-2-298418:europe-west2:movies',
        user='root',
        password='123')
        # conn = pymysql.connect(host='localhost', port=3305, user='root', passwd='123', db='movies')
        # Create a cursor
        cursor = conn.cursor()
        sql = "SELECT * FROM movie WHERE title LIKE " + "'%" + title + "%'" + "ORDER BY imdb DESC"
        # Run sql
        cursor.execute(sql)
        # Match sql statement
        idTitle = cursor.fetchall()
        # print(idTitle)
        # print(type(idTitle))
        # Close cursor
        cursor.close()
        # Close connection
        conn.close()
        # If no result get
        if idTitle == ():
            return render(request, 'getMovieNull.html')
        # cnt = 0
        for movies in idTitle:
            # cnt = cnt + 1
            # netflix
            if movies[6] == 1:
                netflix = "Yes"
            else:
                netflix = "No"
            # hulu
            if movies[7] == 1:
                hulu = "Yes"
            else:
                hulu = "No"
            # primeVideo
            if movies[8] == 1:
                primeVideo = "Yes"
            else:
                primeVideo = "No"
            # disney
            if movies[9] == 1:
                disney = "Yes"
            else:
                disney = "No"
            # Create a dict for passing data to frontend
            m = {"title": movies[1], "year": movies[2], "age": movies[3],
                 "imdb": movies[4], "rottenTomatoes": movies[5], "netflix": netflix,
                 "hulu": hulu, "primeVideo": primeVideo, "disney": disney,
                 "type": movies[10], "directors": movies[11], "genres": movies[12],
                 "country": movies[13], "language": movies[14], "runtime": movies[15]}
            datalist.append(m)
            # if cnt >= 10:
            #     break
    else:
        return render(request, 'index.html')

    return render(request, "getMovie.html", {"data": datalist})
