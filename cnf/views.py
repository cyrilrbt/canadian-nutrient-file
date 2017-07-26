from flask import current_app as app, request, render_template
from cnf.models import (
    CNFFoodName, CNFConversionFactor, CNFNutrientAmount,
    CNFYieldAmount, CNFRefuseAmount
)


@app.route('/', methods=['GET'], endpoint='cnf.index')
def index():
    q = request.args.get('q')
    foods = CNFFoodName.objects.filter(description__icontains=q) if q else []
    return render_template('index.html', foods=foods, q=q)


@app.route('/<int:food_id>', methods=['GET'], endpoint='cnf.show')
def show(food_id):
    food = CNFFoodName.objects.get(id=str(food_id))
    conversions = CNFConversionFactor.objects.filter(food=food)
    nutrients = CNFNutrientAmount.objects.filter(food=food, nutrient_value__gt=0)
    yields = CNFYieldAmount.objects.filter(food=food)
    refuses = CNFRefuseAmount.objects.filter(food=food)
    return render_template(
        'show.html',
        food=food,
        conversions=conversions,
        nutrients=nutrients,
        yields=yields,
        refuses=refuses,
    )
