import json

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Item, Review
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range
from marshmallow import ValidationError

import json


class SchemaAddItemView(Schema):
    title = fields.Str(validate=Length(1, 64), requires=True)
    description = fields.Str(validate=Length(1, 1024))
    price = fields.Int(validate=Range(1, 1000000))    
    
    
class SchemaPostReviewView(Schema):
    text = fields.Str(validate=Length(1, 1024))
    grade = fields.Int(validate=Range(1, 10))
    
    
@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        # Здесь должен быть ваш код
        try:
            document = json.loads(request.body)
            schema = SchemaAddItemView(strict=True)
            data = schema.load(document)
            try:
                title = data[0]['title']
                description = data[0]['description']
                price = data[0]['price']
            except:
                return JsonResponse({'errors': 'invalid JSON'}, status=400)
                
            item = Item.objects.filter(title=title, description=description, price=price)            
            if not item:            
                item = Item.objects.create(title=title, description=description, price=price)
            else:
                item = item[0]
            return JsonResponse({'id': item.id}, status=201, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'invalid JSON'}, status=400)
        except ValidationError as er:
            return JsonResponse({'errors': er.messages}, status=400)            


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        # Здесь должен быть ваш код
        try:
            item = Item.objects.get(id=item_id)
        except:
            return JsonResponse({'error': 'Товар с таким id не существует'}, status=404)
        
        try:
            document = json.loads(request.body)
            schema = SchemaPostReviewView(strict=True)
            data = schema.load(document)
            text = data[0]['text']
            grade = data[0]['grade']            
            review = Review.objects.create(item=Item.objects.get(id=item_id), text=text, grade=grade)
            return JsonResponse({'id': 1}, status=201, safe=False)
        
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'invalid JSON'}, status=400)
        except ValidationError as er:
            return JsonResponse({'errors': er.messages}, status=400)       
        except Exception as error:
            print(error)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        # Здесь должен быть ваш код
        try:
            item = Item.objects.get(id=item_id)
        except:
            return JsonResponse({'error': 'Товар с таким id не существует'}, status=404)        
        
        try:
            reviews = Review.objects.filter(item=item).order_by('-id')[:5]
            data = []
            for review in reviews:
                data.append({'id': review.id, 'text': review.text, 'grade': review.grade})
            
            return JsonResponse({'id': item.id, 'title': item.title, 'description': item.description, 'price': item.price, 'reviews': data}, status=200)
        except Exception as er:
            return JsonResponse({'errors': 'ERROR'}, status=400)
            
