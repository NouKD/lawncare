from django.shortcuts import render

# Create your views here.
def index (request):
    datas={

    }
    return render (request,"index.html", datas)

def about (request):
    datas={

    }
    return render (request,"about.html", datas)

def blog (request):
    datas={

    }
    return render (request,"blog.html", datas)

def gallery (request):
    datas={

    }
    return render (request,"gallery.html", datas)    

def contact (request):
    datas={

    }
    return render (request,"contact.html", datas) 

def services (request):
    datas={

    }
    return render (request,"services.html", datas)


def main (request):
    datas={

    }
    return render (request,"main.html", datas)    

def blog_single (request):
    datas={

    }
    return render (request,"blog-single.html", datas) 

