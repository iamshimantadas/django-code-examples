from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import stripe
from django.urls import reverse
import requests


# class PaymentView(APIView):
#     def post(self, request):

#         user_id = request.data.get("userid")
#         email = request.data.get("email")
#         product_id = request.data.get("product")
#         name = request.data.get("name")


#         try:
#             stripe.api_key = settings.STRIPE_SECRET_KEY

#             product = stripe.Product.retrieve(product_id)
#             price = stripe.Price.retrieve(product.default_price)

#             try:
#                 stripe.Customer.list(email=email, limit=1).data[0]
                
#                 res = stripe.Customer.list(email=email)    
#                 session = stripe.checkout.Session.create(
#                 payment_method_types=["card"],
#                 line_items=[
#                     {
#                         "price": price.id, 
#                         "quantity": 1,
#                     }
#                 ],
#                 mode="payment",
#                 success_url=settings.SUCCESS_URL,
#                 cancel_url=settings.FAILED_URL,
#                 customer_email=email, 
#                 client_reference_id=res.id, 
#                 )

#                 checkout_url = session.url
#                 return Response({"checkout_url": checkout_url})
            
#             except IndexError:
#                 stripe.Customer.create(
#                 name=name,
#                 email=email,
#                 )
                
#                 res = stripe.Customer.list(email=email)
#                 session = stripe.checkout.Session.create(
#                 payment_method_types=["card"],
#                 line_items=[
#                     {
#                         "price": price.id, 
#                         "quantity": 1,
#                     }
#                 ],
#                 mode="payment",
#                 success_url=settings.SUCCESS_URL,
#                 cancel_url=settings.FAILED_URL,
#                 customer_email=email, 
#                 client_reference_id=res.id, 
#                 )

#                 checkout_url = session.url
#                 return Response({"checkout_url": checkout_url})

#                 payment_url = reverse('payment-view')
#                 payment_data = {
#                     'userid': res.id,
#                     'email': email,
#                     'product': request.data.get("product"),
#                     'name': name,
#                 }

#                 response = requests.post(request.build_absolute_uri(payment_url), data=payment_data)
#                 return Response({"message": "created", "customer": res, "payment_response": response.json()})
    

#         except Exception as e:
#             print(e)
#             return Response({"status":"error"})


class PaymentView(APIView):
    def post(self, request):
        try:
            # Extracting data from the request
            email = request.data.get("email")
            product_id = request.data.get("product")
            name = request.data.get("name")

            # Initialize Stripe API key
            stripe.api_key = settings.STRIPE_SECRET_KEY

            # Retrieve product and price information from Stripe
            product = stripe.Product.retrieve(product_id)
            price = stripe.Price.retrieve(product.default_price)

            # Check if the customer already exists
            customer_list = stripe.Customer.list(email=email, limit=1).data

            if customer_list:
                # Customer already exists, use the existing customer
                # customer = customer_list[0]
                 
                customer = stripe.Customer.list(email=email)
                session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price": price.id,
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=settings.SUCCESS_URL,
                cancel_url=settings.FAILED_URL,
                customer_email=email,
                client_reference_id=customer.id,
                )
                checkout_url = session.url
                return Response({"checkout_url": checkout_url})
            
            else:
                # Create a new customer if not exists
                customer = stripe.Customer.create(
                    name=name,
                    email=email,
                )


            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price": price.id,
                        "quantity": 1,
                    }
                ],
                mode="payment",
                success_url=settings.SUCCESS_URL,
                cancel_url=settings.FAILED_URL,
                customer_email=email,
                client_reference_id=customer.id,
            )
            checkout_url = session.url
            return Response({"checkout_url": checkout_url})

        except Exception as e:
            print(e)
            return Response({"status": "error"})


        
@api_view(['GET'])
def ProductsView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    product = stripe.Product.list()
    return Response({"product":product})

@api_view(['GET'])
def SuccessView(request):
    return Response({"message": "payment done"})

@api_view(['GET'])
def FailView(request):
    return Response({"message": "payment failed"})


@api_view(['POST'])
def CreateView(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    try:
        # Extracting data from the request
        name = request.data.get("name")
        email = request.data.get("email")

        # Check if the customer already exists
        customer_list = stripe.Customer.list(email=email, limit=1).data

        if customer_list:
            # return Response({"status": "error", "message": "Customer with this email already exists."})
                payment_url = reverse('payment-view')
                payment_data = {
                    'email': email,
                    'product': request.data.get("product"),
                    'name': name,
                }

                response = requests.post(request.build_absolute_uri(payment_url), data=payment_data)
        else:
                # Create a new customer
                customer = stripe.Customer.create(
                    name=name,
                    email=email,
                )
                # return Response({"message": "created", "customer": customer})

                payment_url = reverse('payment-view')
                payment_data = {
                    'email': email,
                    'product': request.data.get("product"),
                    'name': name,
                }

                response = requests.post(request.build_absolute_uri(payment_url), data=payment_data)

    except Exception as e:
        print(e)
        return Response({"status": "error"})
    
    # try:
    #     name = request.data.get("name")
    #     mail = request.data.get("email")
    #     try:
    #         stripe.Customer.list(email=mail, limit=1).data[0]
    #         return Response({"status": "error", "message": "Customer with this email already exists."})
    #     except IndexError:
    #         res = stripe.Customer.create(
    #         name=name,
    #         email=mail,
    #         )
    #         return Response({"message":"created","customer":res})
        
    # except Exception as e:
    #     print(e)
    #     return Response({"status":"error"})        