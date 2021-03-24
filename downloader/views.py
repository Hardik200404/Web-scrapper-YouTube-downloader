from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube

def home(req):
    if req.method=='POST':
        youtube_url=req.POST['yt-url']
        yt = YouTube(youtube_url)
        thumbnail_url = yt.thumbnail_url
        title = yt.title
        length = yt.length
        desc = yt.description
        view = yt.views
        rating = yt.rating
        age_restricted = yt.age_restricted
        context={
            'title':title,
            'thumbnail':thumbnail_url,
            'video_url':youtube_url,
        }
        return render(req,'download_templates/download.html',context)

    return render(req,'download_templates/home.html')

def downloading(req):
    if req.method=='POST':
        formatRadio=req.POST['formatRadio']
        if formatRadio!='audio':#user when chose video
            qualityRadio=req.POST['qualityRadio']
        video_url=req.POST['video_url_id']
        yt=YouTube(video_url)
        if formatRadio=='audio':
            yt.streams.filter(type=formatRadio).last().download()
        else:
            yt.streams.filter(type=formatRadio,resolution=qualityRadio).first().download()


    context={'msg':"Downloaded Successfully!!"}
    return render(req,'download_templates/downloaded.html',context)

