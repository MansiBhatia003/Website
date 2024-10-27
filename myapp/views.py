from django.shortcuts import render,redirect
from myapp.models import myreview
from myapp.models import myhelp
from myapp.models import mycontact
from myapp.models import userregister
from myapp.models import article
from myapp.models import countries
from myapp.models import cun_details
from myapp.models import universities
from myapp.models import visa
from myapp.models import video

from django.conf  import settings
from django.core.mail import send_mail
import statsmodels.api as sm
from PIL import Image, ImageDraw
import matplotlib
from io import BytesIO
import matplotlib.pyplot as plt
import io
import base64
import warnings
import itertools
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import country_converter as coco
import plotly.graph_objects as go
# Create your views here.
def login(request):
	if request.method =="POST":
		Us=request.POST.get('email')
		Pw=request.POST.get('password')
		expert = userregister.objects.filter(Email=Us, Password= Pw)
		k=len(expert)
		if k>0:
			request.session['Email']= Us
			return render(request,'dashboard.html',{})
		else:
			return render(request,'login.html',{'msg':1})
	else:
		return render(request,'login.html',{})
def changepassword(request):
	if not request.session.has_key('Email'):
		return redirect('/Login')
	if request.method=="POST":
		user=userregister.objects.get(Email=request.session['Email'])
		opass=request.POST.get('old')
		newpass=request.POST.get('new')
		cpass=request.POST.get('cpw')
		if newpass == cpass:
			p=user.Password
			if p == opass:
				user.Password = newpass
				user.CPassword = newpass
				user.save()
				succ="Password successfully changed"
				return render(request,'changepassword.html',{'succ':succ})
			else:
			    err="invalid current password"
			    return render(request,'changepassword.html',{'error':err})
		else:
				err="new and cpass does not match"
				return render(request,'changepassword.html',{'error':err})
	else:
		return render(request,'changepassword.html')
def footer(request):
	return render(request,'footer.html')
def forgot(request):
	if (request.method=="POST"):
		Email=request.POST.get('email')
		user=userregister.objects.filter(Email=Email)
		if (len(user)>0):
			pw=user[0].Password
			subject="password"
			message="Welcome to Gateway.Your password is"+pw
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[Email,]
			send_mail(subject,message,email_from,recipient_list)
			rest="Your password sent to your respective Email Account.Please reset your Password"
			return render(request,'forgot.html',{'rest':rest})
		else:
		    res="This Email id is not registered"
		    return render(request,'forgot.html',{'res':res})
	else:
		return render(request,'forgot.html')	
def header(request):
	return render(request,'header.html')
def help(request):
	if not request.session.has_key('Email'):
		return redirect('/Login')
	if request.method=="POST":
		x=myhelp()
		x.Title   =request.POST.get('title')
		x.message =request.POST.get('msg')
		x.save()
		return render(request,'help.html',{'msg':1})
	else:    
		return render(request,'help.html')
def registration(request):
	if request.method=="POST":
		Firstname=request.POST.get('firstname')
		Lastname=request.POST.get('lastname')
		Email=request.POST.get('email')
		Password=request.POST.get('password')
		CPassword=request.POST.get('cpassword')      
		if Password == CPassword:
			if userregister.objects.filter(Email=Email).exists():
			   return render(request,'registration.html',{'msg':2})
			else:
				x=userregister()
				x.Firstname=Firstname
				x.Lastname=Lastname
				x.Email= Email
				x.Password=Password
				x.CPassword=CPassword
				x.save()
				return render(request,'registration.html',{'msg':3})
		else:
		     return render(request,'registration.html',{'msg':1})
	else:
	     return render(request,'registration.html')	     	        
def review(request):
	if not request.session.has_key('Email'):
		return redirect('/Login')
	if request.method=="POST":
		x=myreview()
		x.Title   =request.POST.get('title')
		x.message =request.POST.get('msg')
		x.save()
		return render(request,'Review.html',{'msg':1})
	else:    
		return render(request,'Review.html')
def sidebar(request):
	return render(request,'sidebar.html')
def contact(request):
	if request.method=="POST":
		x=mycontact()
		x.Name    =request.POST.get('name')
		x.Email   =request.POST.get('email')
		x.Subject =request.POST.get('subject')
		x.Message =request.POST.get('msg')
		x.save()
		return render(request,'Contact.html',{'msg':1})
	else:    
		return render(request,'Contact.html')
def base(request):
	# con=countries.objects.all()
	return render(request,'base.html')
def myprofile(request):
	if not request.session.has_key('Email'):
		return redirect('/Login')
	user=userregister.objects.get(Email=request.session['Email'])
	return render(request,'myprofile.html',{'user':user})
def logout(request):
	if not request.session.has_key('Email'):
		return redirect('/Login')
	del request.session['Email']
	return redirect('/Login')
def viewarticle(request):
	arc=article.objects.all()
	return render(request,'viewarticle.html',{'arc':arc})
def editprofile(request):
	user=userregister.objects.get(Email=request.session['Email'])
	if request.method=='POST':
		detail=userregister.objects.get(Email=request.session['Email'])
		detail.Firstname=request.POST.get('fname')
		detail.Lastname=request.POST.get('lname')
		detail.Email=request.POST.get('email')
		detail.Contact=request.POST.get('telno')
		detail.Gender=request.POST.get('gender')
		detail.Age=request.POST.get('age')
		detail.Address=request.POST.get('addr')
		detail.save()
		user=userregister.objects.get(Email=request.session['Email'])
		return redirect('/profile/',{'i':user})
	else:
		return render(request,'editprofile.html',{'i':user})
def hdianalysis(request):
	return render(request,'hdianalysis.html')
def hdiprediction(request):
	if request.method=="POST":
		year=request.POST.get("year")
		country=request.POST.get("country")
		import pandas as pd
		import statsmodels.api as sm
		import warnings
		import itertools
		import numpy as np
		df = pd.read_csv("human-development-index.csv", parse_dates=['Year'])
		df.columns
		df= df.loc[df['Entity']==country]
		df['Year']= pd.to_datetime(df['Year'])
		country=df.loc[:,['Year','Human Development Index']]
		country= country.sort_values('Year')
		df.isnull().sum()
		country.dtypes
		country = country.set_index('Year')
		country.index
		p=d=q=range(0,2)
		pdq= list(itertools.product(p,d,q))
		seasonal_pdq=[(x[0],x[1],x[2],12)for x in list(itertools.product(p,d,q))]
		min=9999999
		p1=[-1,-1,-1]
		p2=[-1,-1,-1,-1]
		for param in pdq:
			for param_seasonal in seasonal_pdq:
				try:
					mod = sm.tsa.statespace.SARIMAX(country,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
					results = mod.fit()
					if results.aic<min:
						min=results.aic
						p1=param
						p2=param_seasonal
						print('ARIMA{}x{}12 - AIC:{}'.format(param,param_seasonal,results.aic))
				except:
					continue
		print(p1)
		print(min)
		print(p2)
		mod = sm.tsa.statespace.SARIMAX(country,
                                order=(p1[0],p1[1],p2[2]),
            seasonal_order=(p2[0],p2[1],p2[2],12),
            enforce_stationarity=False,
            enforce_invertibility=False)
		results = mod.fit()
		import plotly.graph_objects as go
		results = mod.fit()
		steps=int(request.POST.get('n'))
		pred_uc = results.get_forecast(steps=steps)
		# Create traces
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=country.index, y=country['Human Development Index'],
			mode='lines',
			name='Actual Value'))
		type(pred_uc.predicted_mean)
		fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
			mode='lines',
			name='Predicted Value'))
		fig.update_layout(title='Prediction',
                   xaxis_title='Year',
                   yaxis_title='human-development-index')
		graph=fig.to_html()
		return render(request,'hdiprediction.html',{'graph':graph})
	else:
		return render(request,'hdiprediction.html')
def Gnianalysis(request):
	return render(request,'Gnianalysis.html')
def Gniprediction(request):
	if request.method=="POST":
		year=request.POST.get("year")
		import pandas as pd
		import statsmodels.api as sm
		import warnings
		import itertools
		import numpy as np
		df = pd.read_csv("gross-national-income-per-capita.csv", parse_dates=['Year'])
		df.columns
		df['Year']= pd.to_datetime(df['Year'])
		country=request.POST.get("country")
		df= df.loc[df['Entity']==country]
		country=df.loc[:,['Year','GNI per capita, PPP (constant 2017 international $)']]
		country= country.sort_values('Year')
		df.isnull().sum()
		country.dtypes
		country = country.set_index('Year')
		country.index
		p=d=q=range(0,2)
		pdq= list(itertools.product(p,d,q))
		seasonal_pdq=[(x[0],x[1],x[2],12)for x in list(itertools.product(p,d,q))]
		min=9999999
		p1=[-1,-1,-1]
		p2=[-1,-1,-1,-1]
		for param in pdq:
			for param_seasonal in seasonal_pdq:
				try:
					mod = sm.tsa.statespace.SARIMAX(country,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
					results = mod.fit()
					if results.aic<min:
						min=results.aic
						p1=param
						p2=param_seasonal
						print('ARIMA{}x{}12 - AIC:{}'.format(param,param_seasonal,results.aic))
				except:
					continue
		print(p1)
		print(min)
		print(p2)
		import plotly.graph_objects as go
		results = mod.fit()
		steps=int(request.POST.get('n'))
		pred_uc = results.get_forecast(steps=steps)
		# Create traces
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=country.index, y=country['GNI per capita, PPP (constant 2017 international $)'],
			mode='lines',
        	name='Actual Value'))
		type(pred_uc.predicted_mean)
		fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
			mode='lines',
			name='Predicted Value'))
		fig.update_layout(title='Prediction ',
                   xaxis_title='Year',
                   yaxis_title='gross-national-income')       
		graph=fig.to_html()
		return render(request,'Gniprediction.html',{'graph':graph})
	else:
		return render(request,'Gniprediction.html')
def happanalysis(request):
	return render(request,'happanalysis.html')
def happprediction(request):
	if request.method=="POST":
		year=request.POST.get("year")
		import pandas as pd
		import statsmodels.api as sm
		import warnings
		import itertools
		import numpy as np
		df = pd.read_csv("happiness.csv", parse_dates=['Year'])
		df.columns
		country=request.POST.get("country")
		df= df.loc[df['Entity']==country]
		df['Year']= pd.to_datetime(df['Year'])
		country=df.loc[:,['Year','Happiness Index']]
		country= country.sort_values('Year')
		df.isnull().sum()
		country.dtypes
		country = country.set_index('Year')
		country.index
		p=d=q=range(0,2)
		pdq= list(itertools.product(p,d,q))
		seasonal_pdq=[(x[0],x[1],x[2],12)for x in list(itertools.product(p,d,q))]
		min=9999999
		p1=[-1,-1,-1]
		p2=[-1,-1,-1,-1]
		for param in pdq:
			for param_seasonal in seasonal_pdq:
				try:
					mod = sm.tsa.statespace.SARIMAX(country,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
					results = mod.fit()
					if results.aic<min:
						min=results.aic
						p1=param
						p2=param_seasonal
						print('ARIMA{}x{}12 - AIC:{}'.format(param,param_seasonal,results.aic))
				except:
					continue
		print(p1)
		print(min)
		print(p2)
		mod = sm.tsa.statespace.SARIMAX(country,
                                order=(p1[0],p1[1],p2[2]),
            seasonal_order=(p2[0],p2[1],p2[2],12),
            enforce_stationarity=False,
            enforce_invertibility=False)
		results = mod.fit()
		import plotly.graph_objects as go
		results = mod.fit()
		steps=int(request.POST.get('n'))
		pred_uc = results.get_forecast(steps=steps)
		# Create traces
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=country.index, y=country['Happiness Index'],
			mode='lines',
			name='Actual Value'))
		type(pred_uc.predicted_mean)
		fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
			mode='lines',
			name='Predicted Value'))
		fig.update_layout(title='Prediction ',
                   xaxis_title='Year',
                   yaxis_title='Happiness Index')
		graph=fig.to_html()
		return render(request,'happprediction.html',{'graph':graph})
	else:
		return render(request,'happprediction.html')
def lifeanalysis(request):
	return render(request,'lifeanalysis.html')
def lifeprediction(request):
	if request.method=="POST":
		year=request.POST.get("year")
		country=request.POST.get("country")
		import pandas as pd
		import statsmodels.api as sm
		import warnings
		import itertools
		import numpy as np
		df = pd.read_csv("life-expectancy.csv", parse_dates=['Year'])
		df.columns
		df= df.loc[df['Entity']==country]
		df['Year']= pd.to_datetime(df['Year'])
		country=df.loc[:,['Year','Life expectancy at birth (historical)']]
		country= country.sort_values('Year')
		df.isnull().sum()
		country.dtypes
		country = country.set_index('Year')
		country.index
		p=d=q=range(0,2)
		pdq= list(itertools.product(p,d,q))
		seasonal_pdq=[(x[0],x[1],x[2],12)for x in list(itertools.product(p,d,q))]
		min=9999999
		p1=[-1,-1,-1]
		p2=[-1,-1,-1,-1]
		for param in pdq:
		    for param_seasonal in seasonal_pdq:
		        try:
		            mod = sm.tsa.statespace.SARIMAX(country,
		                                            order=param,
		                                            seasonal_order=param_seasonal,
		                                            enforce_stationarity=False,
		                                            enforce_invertibility=False)
					results = mod.fit()
					if results.aic<min:
						min=results.aic
						p1=param
						p2=param_seasonal
					print('ARIMA{}x{}12 - AIC:{}'.format(param,param_seasonal,results.aic))
				except:
					continue
		print(p1)
		print(min)
		print(p2)
		mod = sm.tsa.statespace.SARIMAX(country,
                                order=(p1[0],p1[1],p2[2]),
                                seasonal_order=(p2[0],p2[1],p2[2],12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
		results = mod.fit()
		import plotly.graph_objects as go
		results = mod.fit()
		steps=int(request.POST.get('n'))
		pred_uc = results.get_forecast(steps=steps)
		# Create traces
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=country.index, y=country['Life expectancy at birth (historical)'],
                         mode='lines',
                         name='Actual Value'))
		type(pred_uc.predicted_mean)
		fig.add_trace(go.Scatter(x=pred_uc.predicted_mean.index, y=pred_uc.predicted_mean,
                         mode='lines',
                         name='Predicted Value'))
		fig.update_layout(title='Prediction ',
                   xaxis_title='Year',
                   yaxis_title='Life Expectancy')
		graph=fig.to_html()
		return render(request,'lifeprediction.html',{'graph':graph})
	else:
		return render(request,'lifeprediction.html')
def g1(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		print(df.columns)
		Entity=request.POST.get('country')
		dfa=df[df['Entity']==Entity]
		fig = px.line(dfa, x="Year", y="GNI per capita, PPP (constant 2017 international $)",title='GNI PER CAPITA')
		#fig.show()
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'g1.html',{'graph':graph})
	else:
		return render(request,'g1.html')
def g2(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		print(df.columns)
		Entity= request.POST.get('country')
		dfa=df[df['Entity']==Entity]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dff=dfa[(dfa['Year']>=year1) & (dfa['Year']<=year2)]
		fig = px.line(dff, x="Year", y="GNI per capita, PPP (constant 2017 international $)",title='Gross naotional income',text="Year")
		fig.update_traces(textposition="top right")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'g2.html',{'graph':graph})
	else:	
		return render(request,'g2.html')
	return render(request,'g2.html')
def g3(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Gross National Income per capita in both countries',
                   xaxis_title='Year',
                   yaxis_title='gross-national-income')
		graph=fig.to_html()
		return render(request,'g3.html',{'graph':graph})
	else:
		return render(request,'g3.html')
def g4(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Gross National Income in both countries',
                   xaxis_title='Year',
                   yaxis_title='gross-national-income')
		graph=fig.to_html()
		return render(request,'g4.html',{'graph':graph})
	else:
		return render(request,'g4.html')
def g5(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Gross National Income in following countries',
                   xaxis_title='Year',
                   yaxis_title='gross-national-income')
		graph=fig.to_html()
		return render(request,'g5.html',{'graph':graph})
	else:
		return render(request,'g5.html')
def g6(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		df3=df3[(df3['Year']>=year1) & (df3['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['GNI per capita, PPP (constant 2017 international $)'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Gross National Income in following countries',
                   xaxis_title='Year',
                   yaxis_title='gross-national-income')
		graph=fig.to_html()
		return render(request,'g6.html',{'graph':graph})
	else:
		return render(request,'g6.html')
def g7(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='GNI per capita, PPP (constant 2017 international $)')
		n=int(request.POST.get('cn'))
		dfmax=df1.tail(n)
		fig = px.bar(dfmax, x='Entity', y='GNI per capita, PPP (constant 2017 international $)',text_auto='.2s',title="Gross National Income in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'g7.html',{'graph':graph})
	else:	
		return render(request,'g7.html')
def g8(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='GNI per capita, PPP (constant 2017 international $)')
		n=int(request.POST.get('cn'))
		dfmin=df1.head(n)
		fig = px.bar(dfmin, x='Entity', y='GNI per capita, PPP (constant 2017 international $)',text_auto='.2s',title="Gross National Income in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'g8.html',{'graph':graph})
	else:	
		return render(request,'g8.html')
	return render(request,'g8.html')
def g9(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		cc= coco.CountryConverter()
		df['Entity-codes']= coco.convert(names=df['Code'], to='ISO3')
		print(df['Entity-codes'])
		fig = px.scatter_geo(df, locations="Entity-codes", color="Year",
                     hover_name="Entity", size="GNI per capita, PPP (constant 2017 international $)",animation_frame="Year",
                     projection="natural earth")
		year=request.POST.get('year')
		graph=fig.to_html()
		return render(request,'g9.html',{'graph':graph})
	else:
		return render(request,'g9.html')
def g10(request):
	if request.method=='POST':
		df = pd.read_csv('gross-national-income-per-capita.csv')
		country=request.POST.get('country')
		dfc=df[df['Entity']==country]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		fig = px.scatter(dfc, x="Year", y="GNI per capita, PPP (constant 2017 international $)",
	         size="GNI per capita, PPP (constant 2017 international $)", color="Year",
                 hover_name="Entity", log_x=True, size_max=60,title="Gross National Income")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'g10.html',{'graph':graph})
	else:	
		return render(request,'g10.html')
def h1(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		print(df.columns)
		Entity=request.POST.get('country')
		dfa=df[df['Entity']==Entity]
		fig = px.line(dfa, x="Year", y="Happiness Index",title='happiness-index')
		#fig.show()
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'h1.html',{'graph':graph})
	else:
		return render(request,'h1.html')
def h2(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		print(df.columns)
		Entity= request.POST.get('country')
		dfa=df[df['Entity']==Entity]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dff=dfa[(dfa['Year']>=year1) & (dfa['Year']<=year2)]
		fig = px.line(dff, x="Year", y="Happiness Index",title='Happiness Index',text="Year")
		fig.update_traces(textposition="top right")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'h2.html',{'graph':graph})
	else:	
		return render(request,'h2.html')
	return render(request,'h2.html')
def h3(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Happiness Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Happiness Index'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Happiness Index in both countries',
                   xaxis_title='Year',
                   yaxis_title='Happiness Index')
		graph=fig.to_html()
		return render(request,'h3.html',{'graph':graph})
	else:
		return render(request,'h3.html')
def h4(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Happiness Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Happiness Index'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Happiness Index in both countries',
                   xaxis_title='Year',
                   yaxis_title='happiness-index')
		graph=fig.to_html()
		return render(request,'h4.html',{'graph':graph})
	else:
		return render(request,'h4.html')
def h5(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Happiness Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Happiness Index'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Happiness Index'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Happiness Index in following countries',
                   xaxis_title='Year',
                   yaxis_title='happiness-index')
		graph=fig.to_html()
		return render(request,'h5.html',{'graph':graph})
	else:
		return render(request,'h5.html')
def h6(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		df3=df3[(df3['Year']>=year1) & (df3['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Happiness Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Happiness Index'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Happiness Index'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Happiness Index in both countries',
                   xaxis_title='Year',
                   yaxis_title='happiness-index')
		graph=fig.to_html()
		return render(request,'h6.html',{'graph':graph})
	else:
		return render(request,'h6.html')
def h7(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='Happiness Index')
		n=int(request.POST.get('cn'))
		dfmax=df1.tail(n)
		fig = px.bar(dfmax, x='Entity', y='Happiness Index',text_auto='.2s',title="Happiness Index in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'h7.html',{'graph':graph})
	else:	
		return render(request,'h7.html')
def h8(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='Happiness Index')
		n=int(request.POST.get('cn'))
		dfmin=df1.head(n)
		fig = px.bar(dfmin, x='Entity', y='Happiness Index',text_auto='.2s',title="Happiness Index in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'h8.html',{'graph':graph})
	else:	
		return render(request,'h8.html')
def h9(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		cc= coco.CountryConverter()
		df['Entity-codes']= coco.convert(names=df['Code'], to='ISO3')
		print(df['Entity-codes'])
		fig = px.scatter_geo(df, locations="Entity-codes", color="Entity",
                     hover_name="Entity", size="Happiness Index",animation_frame="Year",
                     projection="natural earth")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'h9.html',{'graph':graph})
	else:
		return render(request,'h9.html')
def h10(request):
	if request.method=='POST':
		df = pd.read_csv('happiness.csv')
		country=request.POST.get('country')
		dfc=df[df['Entity']==country]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		fig = px.scatter(dfc, x="Year", y="Happiness Index",
	         size="Happiness Index", color="Year",
                 hover_name="Entity", log_x=True, size_max=60,title="Happiness Index")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'h10.html',{'graph':graph})
	else:	
		return render(request,'h10.html')
def hdi1(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		print(df.columns)
		Entity=request.POST.get('country')
		dfa=df[df['Entity']==Entity]
		fig = px.line(dfa, x="Year", y="Human Development Index",title='human-development-index')
		#fig.show()
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'hdi1.html',{'graph':graph})
	else:
		return render(request,'hdi1.html')
def hdi2(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		print(df.columns)
		Entity= request.POST.get('country')
		dfa=df[df['Entity']==Entity]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dff=dfa[(dfa['Year']>=year1) & (dfa['Year']<=year2)]
		fig = px.line(dff, x="Year", y="Human Development Index",title='Human Development Index',text="Year")
		fig.update_traces(textposition="top right")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'hdi2.html',{'graph':graph})
	else:	
		return render(request,'hdi2.html')
def hdi3(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Human Development Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Human Development Index'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Human Development Index in both countries',
                   xaxis_title='Year',
                   yaxis_title='Human Development Index')
		graph=fig.to_html()
		return render(request,'hdi3.html',{'graph':graph})
	else:
		return render(request,'hdi3.html')
def hdi4(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Human Development Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Human Development Index'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Human Development Index in both countries',
                   xaxis_title='Year',
                   yaxis_title='human-development-index')
		graph=fig.to_html()
		return render(request,'hdi4.html',{'graph':graph})
	else:
		return render(request,'hdi4.html')
def hdi5(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Human Development Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Human Development Index'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Human Development Index'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Human Development Index in both countries',
                   xaxis_title='Year',
                   yaxis_title='human-development-index')
		graph=fig.to_html()
		return render(request,'hdi5.html',{'graph':graph})
	else:
		return render(request,'hdi5.html')
def hdi6(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		df3=df3[(df3['Year']>=year1) & (df3['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Human Development Index'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Human Development Index'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Human Development Index'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Human Development Index in both countries',
                   xaxis_title='Year',
                   yaxis_title='human-development-index')
		graph=fig.to_html()
		return render(request,'hdi6.html',{'graph':graph})
	else:
		return render(request,'hdi6.html')
def hdi7(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='Human Development Index')
		n=int(request.POST.get('cn'))
		dfmax=df1.tail(n)
		fig = px.bar(dfmax, x='Entity', y='Human Development Index',text_auto='.2s',title="Human Development Index in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'hdi7.html',{'graph':graph})
	else:	
		return render(request,'hdi7.html')
def hdi8(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='Human Development Index')
		n=int(request.POST.get('cn'))
		dfmin=df1.head(n)
		fig = px.bar(dfmin, x='Entity', y='Human Development Index',text_auto='.2s',title="Human Development Index in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'hdi8.html',{'graph':graph})
	else:	
		return render(request,'hdi8.html')
def hdi9(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		cc= coco.CountryConverter()
		df['Entity-codes']= coco.convert(names=df['Code'], to='ISO3')
		print(df['Entity-codes'])
		fig = px.scatter_geo(df, locations="Entity-codes", color="Entity",
                     hover_name="Entity", size="Human Development Index",animation_frame="Year",
                     projection="natural earth")
		graph=fig.to_html()
		return render(request,'hdi9.html',{'graph':graph})
	else:
		return render(request,'hdi9.html')
def hdi10(request):
	if request.method=='POST':
		df = pd.read_csv('human-development-index.csv')
		country=request.POST.get('country')
		dfc=df[df['Entity']==country]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		fig = px.scatter(dfc, x="Year", y="Human Development Index",
	         size="Human Development Index", color="Year",
                 hover_name="Entity", log_x=True, size_max=60,title="Human Development Index")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'hdi10.html',{'graph':graph})
	else:	
		return render(request,'hdi10.html')
def L1(request):
    if request.method=='POST':
    	df = pd.read_csv('life-expectancy.csv')
    	print(df.columns)
    	Entity=request.POST.get('country')
    	dfa=df[df['Entity']==Entity]
    	fig = px.line(dfa, x="Year", y="Life expectancy at birth (historical)",title='life_expectancy')
    	#fig.show()
    	country=request.POST.get('country')
    	graph=fig.to_html()
    	return render(request,'L1.html',{'graph':graph})
    else:
        return render(request,'L1.html')	    
def L2(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		print(df.columns)
		Entity= request.POST.get('country')
		dfa=df[df['Entity']==Entity]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dff=dfa[(dfa['Year']>=year1) & (dfa['Year']<=year2)]
		fig = px.line(dff, x="Year", y="Life expectancy at birth (historical)",title='life_expectancy',text="Year")
		fig.update_traces(textposition="top right")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'L2.html',{'graph':graph})
	else:	
		return render(request,'L2.html')
def L3(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Life expectancy at birth (historical)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Life expectancy at birth (historical)'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Life expectancy in both countries',
                   xaxis_title='Year',
                   yaxis_title='life_expectancy')
		graph=fig.to_html()
		return render(request,'L3.html',{'graph':graph})
	else:
		return render(request,'L3.html')
def L4(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Life expectancy at birth (historical)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Life expectancy at birth (historical)'],
                    mode='lines+markers',
                    name=c2))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		fig.update_layout(title='Life expectancy in both countries',
                   xaxis_title='Year',
                   yaxis_title='life_expectancy')
		graph=fig.to_html()
		return render(request,'L4.html',{'graph':graph})
	else:
		return render(request,'L4.html')
def L5(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Life expectancy at birth (historical)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Life expectancy at birth (historical)'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Life expectancy at birth (historical)'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Life expectancy in both countries',
                   xaxis_title='Year',
                   yaxis_title='life_expectancy')
		graph=fig.to_html()
		return render(request,'L5.html',{'graph':graph})
	else:
		return render(request,'L5.html')
def L6(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		c1=request.POST.get('Fcountry')
		c2=request.POST.get('Scountry')
		c3=request.POST.get('Tcountry')
		df1 = df[df['Entity']==c1]
		df2 = df[df['Entity']==c2]
		df3 = df[df['Entity']==c3]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		df1=df1[(df1['Year']>=year1) & (df1['Year']<=year2)]
		df2=df2[(df2['Year']>=year1) & (df2['Year']<=year2)]
		df3=df3[(df3['Year']>=year1) & (df3['Year']<=year2)]
		fig = go.Figure()
		fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Life expectancy at birth (historical)'],
                    mode='lines',
                    name=c1))
		fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Life expectancy at birth (historical)'],
                    mode='lines+markers',
                    name=c2))
		fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Life expectancy at birth (historical)'],
                    mode='lines+markers',
                    name=c3))
		country=request.POST.get('Fcountry')
		country=request.POST.get('Scountry')
		country=request.POST.get('Tcountry')
		fig.update_layout(title='Life expectancy in both countries',
                   xaxis_title='Year',
                   yaxis_title='life_expectancy')
		graph=fig.to_html()
		return render(request,'L6.html',{'graph':graph})
	else:
		return render(request,'L6.html')
def L7(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='Life expectancy at birth (historical)')
		n=int(request.POST.get('cn'))
		dfmax=df1.tail(n)
		fig = px.bar(dfmax, x='Entity', y='Life expectancy at birth (historical)',text_auto='.2s',title="Life Expectancy in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'L7.html',{'graph':graph})
	else:	
		return render(request,'L7.html')
def L8(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		year = int(request.POST.get('year'))
		df1=df[df["Year"]== year]
		df1=df1.sort_values(by='Life expectancy at birth (historical)')
		n=int(request.POST.get('cn'))
		dfmin=df1.head(n)
		fig = px.bar(dfmin, x='Entity', y='Life expectancy at birth (historical)',text_auto='.2s',title="Life Expectancy in no of countries")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'L8.html',{'graph':graph})
	else:	
		return render(request,'L8.html')
def L9(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		cc= coco.CountryConverter()
		df['Entity-codes']= coco.convert(names=df['Code'], to='ISO3')
		fig = px.scatter_geo(df, locations="Entity-codes", color="Entity",
                     hover_name="Entity", size="Life expectancy at birth (historical)",animation_frame="Year",
                     projection="natural earth")
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'L9.html',{'graph':graph})
	else:	
		return render(request,'L9.html')
def L10(request):
	if request.method=='POST':
		df = pd.read_csv('life-expectancy.csv')
		country=request.POST.get('country')
		dfc=df[df['Entity']==country]
		year1=int(request.POST.get('Syear'))
		year2=int(request.POST.get('Eyear'))
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
		fig = px.scatter(dfc, x="Year", y="Life expectancy at birth (historical)",
	         size="Life expectancy at birth (historical)", color="Year",
                 hover_name="Entity", log_x=True, size_max=60)
		country=request.POST.get('country')
		graph=fig.to_html()
		return render(request,'L10.html',{'graph':graph})
	else:	
		return render(request,'L10.html')
def Astudy(request):
	return render(request,'Astudy.html')
def latestnews(request):
	import datetime
	from datetime import date
	from newsapi.newsapi_client import NewsApiClient
	newsapi= NewsApiClient(api_key='02fd106452cf4b79b266dfaaa7b7f256')
	json_data = newsapi.get_everything(q='Abroad Students',
		                                language='en',
		                                from_param=str(date.today()-datetime.timedelta(days=29)),
		                                to=str(date.today()),
		                                page_size=24,
		                                page=2,
		                                sort_by='relevancy'
)
	k=json_data['articles']
	return render(request,'latestnews.html',{'k':k})
def viewcountries(request):
	con=countries.objects.all()
	return render(request,'viewcountries.html',{'con':con})
def countrydetails(request,name):
	cun=cun_details.objects.filter(Countryname=name)
	return render(request,'countrydetails.html',{'cun':cun})
def viewuni(request):
	uni=universities.objects.all()
	return render(request,'viewuni.html',{'uni':uni})
def it(request):
	return render(request,'ilets.html')
def pte(request):
	return render(request,'pte.html')
def spoken(request):
	return render(request,'spoken.html')
def sat(request):
	return render(request,'sat.html')
def viewvisa(request):
	x=countries.objects.all()
	return render(request,'Visa.html',{'data':x})
def viewvisadetail(request,name):
	v=visa.objects.filter(Countryvisa=name)
	return render(request,'vvisa.html',{'visa':v})
def find(request):
	return render(request,'find.html')
def tips(request):
	return render(request,'tips.html')
def artdetail(request,id):
	x=article.objects.get(id=id)
	return render(request,'artdetail.html',{'i':x})
def about(request):
	return render(request,'about.html')
def dashboard(request):
	return render(request,'dashboard.html')
def viewvideo(request):
	x=video.objects.all()
	return render(request,'viewvideo.html',{'data':x})