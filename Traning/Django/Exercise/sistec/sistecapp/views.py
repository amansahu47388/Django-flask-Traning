from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    s = """<h1 style="color:blue; text-align:center">Sagar Group of Institutions</h1>
    <br>
    <p>Sagar Group of Institutions which was established in the year 2007 under the aegis of Shri Agrawal Educational & Welfare Society with the main objective of imparting quality education.
    Sagar Group of Institutions have emerged as a group of Best Private Colleges in Bhopal with its state-of-the-art facility and its expertise in Engineering, Pharmacy, and MBA education. Three institutional campuses rich in infrastructure and amenities proudly flourish under the aegis of the brand Sagar Group of Institutions
    The brand has a strong motivation towards innovation in curriculum implementation with its unique industry-oriented pedagogy. It further aspires to be a part of an educational revolution in technical education, impacting advanced futuristic technologies in the national and international framework, and aims to be one of the finest providers of technical education in India.</p>

    <img src="https://www.sistec.ac.in/assets/upload/home-sliders/home-slider-380478892.jpg" style="length:1000px; width:1500px">"""
    return HttpResponse(s)

def about(request):
    s= """<h1 style="color:blue; text-align:center">About page</h1>

    <p>Sagar Institute of Science and Technology (SISTec) was established in the year 2007 and with its empirical academic methodologies, state-of-art infrastructure, and facilities, SISTec has become a preferred destination for recruiters and engineering aspirants.
    In a very short span of time, SISTec has become one of the best engineering colleges in Bhopal. Since its inception, the engineering college has carved a niche for itself, and with it being NAAC Accredited College, SISTec aims to be featured in the list of best engineering colleges in India.
    Housed in the picturesque lush green campus in Gandhi Nagar Bhopal, SISTec over the years has proved and lived up to its commitment of delivering high-quality technical education at par with the dynamic technical scenario across the globe.
    SISTec inculcates the spirit of entrepreneurship in students with the Entrepreneurship Development Cell (EDC) dedicated to unearthing the hidden entrepreneurial skills among the technocrats and nurturing them into real start-up initiatives. Many students have been benefited from the formation of this cell and under its banner, they have successfully started their ventures. SISTec was selected for establishing Institution Innovation Council (IIC) at its premises by the Ministry of Human Resource and Development (MHRD), Government of India which helped it a lot in maintaining the status of the best engineering colleges in Bhopal. Under this council, SISTec was able to conduct series of seminars/webinars/workshops/sessions from various experts of the industries. Inter-disciplinary and practical approach in regular academic delivery, emphasis on the overall growth of students, excellent facilities, constant innovation in teaching and training, best placement initiatives, and regular campus recruitment training programs are the key features that SISTec strives on. Affiliated to Rajiv Gandhi Proudyogiki Vishwavidyalaya (RGPV) and approved by the All India Council for Technical Education (AICTE), SISTec offers engineering courses in different disciplines at both undergraduate (B. Tech.) and postgraduate (M. Tech.) level.</p>
    
    """
# Create your views here.
