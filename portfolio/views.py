#from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer

# signup
#from efsblog.portfolio.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# end signup

def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})

# for signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            #return redirect('home')
            # this is working
            return render(request, 'portfolio/home.html', {'portfolio': home})
            #return render(request, 'registration/login.html',{'registration':login})

    else:
        form = SignUpForm()
    return render(request, 'portfolio/signup.html', {'form': form})

# end of signup

@login_required
def customer_list(request):
   customer = Customer.objects.filter(created_date__lte=timezone.now())
   return render(request, 'portfolio/customer_list.html',
                 {'customers': customer})


@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/customer_list.html',
                         {'customers': customer})
   else:
       # edit
       form = CustomerForm(instance=customer)
   return render(request, 'portfolio/customer_edit.html', {'form': form})


@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('portfolio:customer_list')


@login_required
def stock_list(request):
   stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/stock_list.html', {'stocks': stocks})


@login_required
def stock_new(request):
   if request.method == "POST":
       form = StockForm(request.POST)
       if form.is_valid():
           stock = form.save(commit=False)
           stock.created_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html',
                         {'stocks': stocks})
   else:
       form = StockForm()
       # print("Else")
   return render(request, 'portfolio/stock_new.html', {'form': form})


@login_required
def stock_edit(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   if request.method == "POST":
       form = StockForm(request.POST, instance=stock)
       if form.is_valid():
           stock = form.save()
           # stock.customer = stock.id
           stock.updated_date = timezone.now()
           stock.save()
           stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
           return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
   else:
       # print("else")
       form = StockForm(instance=stock)
   return render(request, 'portfolio/stock_edit.html', {'form': form})


@login_required
def stock_delete(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   stock.delete()
   stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
   return render(request, 'portfolio/stock_list.html', {'stocks': stocks})


@login_required
def investment_list(request):
   investments = Investment.objects.filter(acquired_date__lte=timezone.now())
   return render(request, 'portfolio/investment_list.html', {'investments': investments})
# Srav Code begin

@login_required
def investment_new(request):
   if request.method == "POST":
       form = InvestmentForm(request.POST)
       if form.is_valid():
           investment= form.save(commit=False)
           investment.created_date = timezone.now()
           investment.save()
           investments = Investment.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html',
                         {'investments': investments})
   else:
       form = InvestmentForm()
       # print("Else")
   return render(request, 'portfolio/investment_new.html', {'form': form})


@login_required
def investment_edit(request, pk):
   investment= get_object_or_404(Investment, pk=pk)
   if request.method == "POST":
       form = InvestmentForm(request.POST, instance=investment)
       if form.is_valid():
           investment= form.save()
           # investment.customer = investment.id
           investment.updated_date = timezone.now()
           investment.save()
           investments = investment.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/investment_list.html', {'investments': investments})
   else:
       # print("else")
       form = InvestmentForm(instance=investment)
   return render(request, 'portfolio/investment_edit.html', {'form': form})


@login_required
def investment_delete(request, pk):
   investment = get_object_or_404(Investment, pk=pk)
   investment.delete()
   investments = investment.objects.filter(acquired_date__lte=timezone.now())
   return render(request, 'portfolio/investment_list.html', {'investment': investment})
# srav code ends
# Srav code mutual funds begin


@login_required
def mutualfunds_list(request):
   mutualfunds = MutualFunds.objects.filter(acquired_date__lte=timezone.now())
   return render(request, 'portfolio/mutualfunds_list.html', {'mutualfunds': mutualfunds})


@login_required
def mutualfunds_new(request):
   if request.method == "POST":
       form = MutualFundsForm(request.POST)
       if form.is_valid():
           mutualfunds= form.save(commit=False)
           mutualfunds.created_date = timezone.now()
           mutualfunds.save()
           mutualfunds = MutualFunds.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/mutualfunds_list.html',
                         {'mutualfunds': mutualfunds})
   else:
       form = MutualFundsForm()
       # print("Else")
   return render(request, 'portfolio/mutualfunds_new.html', {'form': form})


@login_required
def mutualfunds_edit(request, pk):
   mutualfunds= get_object_or_404(MutualFunds, pk=pk)
   if request.method == "POST":
       form = MutualFundsForm(request.POST, instance=mutualfunds)
       if form.is_valid():
           mutualfunds= form.save()
           # investment.customer = investment.id
           mutualfunds.updated_date = timezone.now()
           mutualfunds.save()
           mutualfunds = mutualfunds.objects.filter(acquired_date__lte=timezone.now())
           return render(request, 'portfolio/mutualfunds_list.html', {'mutualfunds': mutualfunds})
   else:
       # print("else")
       form = MutualFundsForm(instance=mutualfunds)
   return render(request, 'portfolio/mutualfunds_edit.html', {'form': form})


@login_required
def mutualfunds_delete(request, pk):
   mutualfunds = get_object_or_404(MutualFunds, pk=pk)
   mutualfunds.delete()
   mutualfunds = mutualfunds.objects.filter(acquired_date__lte=timezone.now())
   return render(request, 'portfolio/mutualfunds_list.html', {'mutualfunds': mutualfunds})

#srav code mutual funds end

@login_required
def portfolio(request,pk):
   customer = get_object_or_404(Customer, pk=pk)
   customers = Customer.objects.filter(created_date__lte=timezone.now())
   investments =Investment.objects.filter(customer=pk)
   #Srav added mutualfunds
   mutualfunds =MutualFunds.objects.filter(customer=pk)
   stocks = Stock.objects.filter(customer=pk)
   #sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(Sum('acquired_value'))
   sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(Sum('acquired_value'))
   #sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(sum_acq=Sum('acquired_value'))
   sum_recent_value = Investment.objects.filter(customer=pk).aggregate(Sum('recent_value'))
   result =  Investment.objects.filter(customer=pk).aggregate(sum_result = Sum('recent_value') - Sum('acquired_value'))
   #sum_initial_stock_value = Stock.objects.filter(customer=pk).aggregate(Sum('initial_stock_value'))
   sum_initial_stock_value = Stock.objects.filter(customer=pk).aggregate(total=Sum('shares', field="shares*purchase_price"))
   purch_price=Stock.objects.filter(customer=pk).aggregate(pp=Sum('purchase_price'))
   sum_initial_mutualfunds = MutualFunds.objects.filter(customer=pk).aggregate(sum_mf= Sum('acquired_value'))
   sum_final_mutualfunds = MutualFunds.objects.filter(customer=pk).aggregate(sum_final_mf=Sum('recent_value'))
   #sum_current_stock_value = Stock.objects.filter(customer=pk).aggregate(sum_curr=Sum('stocks.current_stock_value'))
   #stock_result = Stock.objects.objects.filter(customer=pk).aggregate(sum_stock_result = Sum('current_stock_value') - Sum('initial_stock_value'))
   #sum_current_stock_value = Stock.objects.filter(customer=pk).aggregate(sum_recent_val=Sum('shares', field="stocks.current_stock_price*shares"))

   stock_list = []
   sum1 = 0

   #for i in stocks:
   #    yahoo = Share(i.symbol)
   #    va = yahoo.get_price()
   #    va2 = float(va) * float(i.shares)
   #    stock_list.append(va)
   #    sum1 = sum1 + float(va) * float(i.shares)

   # Initialize the value of the stocks
   sum_current_stocks_value = 0
   sum_of_initial_stock_value = 0

   for  stock in stocks:
       sum_current_stocks_value += stock.current_stock_value()
       sum_of_initial_stock_value += stock.initial_stock_value()

       #sum1 =  sum1 + float(stock.current_stocks_value()) * float(stock.shares)
       sum1 = sum_current_stocks_value

   for k, v in sum_acquired_value.items():
           var1 = v
   for k, v in sum_recent_value.items():
           var2 = v

   sum = 0
   for i in stocks:
           sum = sum + i.shares * i.purchase_price
           #sum = sum + i.initial_stock_value()



   sum_initial_mf = 0
   for i in mutualfunds:
    sum_initial_mf = sum_initial_mf + i.units * i.acquired_value

   sum_init_inv =0
   for i in  investments:
           sum_init_inv = sum_init_inv + i.acquired_value

   port_init = 0
   port_init = sum + sum_init_inv + sum_initial_mf


   sum_final_inv =0
   for i in investments:
           sum_final_inv= sum_final_inv +i.recent_value

   sum_final_mf=0
   for i in mutualfunds:
            sum_final_mf= sum_final_mf + i.units * i.recent_value

   port_final =0
   port_final = float(sum1) + float(sum_final_inv) + float(sum_final_mf)



   return render(request, 'portfolio/portfolio.html', {'customers': customers, 'investments': investments,'mutualfunds':mutualfunds,
                                                      'stocks': stocks,'sum_acquired_value': sum_acquired_value,
                                                       'sum_recent_value': sum_recent_value, 'result':result,
                                                       'sum_initial_stock_value': sum,
                                                       'purch_price':purch_price,
                                                       'sum_initial_mutualfunds':sum_initial_mutualfunds,
                                                       'sum_final_mutualfunds':sum_final_mutualfunds
                                                       ,'sum_current_stock_value':sum_current_stocks_value
                                                       ,'Portfolio_Initial' : port_init
                                                       ,'Sum_Init_MF':sum_initial_mf
                                                       ,'Sum_Init_Investment': sum_init_inv
                                                       ,'Sum_Final_MF': float(sum_final_mf)
                                                       ,'Porfolio_Final': port_final
                                                       ,'Sum_Final_Invst': sum_final_inv



                                                       })



class CustomerList(APIView):

    def get(self,request):
        customers_json = Customer.objects.all()
        serializer = CustomerSerializer(customers_json, many=True)
        return Response(serializer.data)


