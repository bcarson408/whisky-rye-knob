from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,Form,TextAreaField,FormField,FieldList
# from wtforms.validators import InputRequired,Length,AnyOf
from wtforms.widgets import html_params


class IngredientForm(Form):
    ingredient = StringField("Cocktial Ingredient")
    ounce = StringField("Ounce Pour")

class CocktailForm1(Form):
    name = StringField("name")
    cocktail_ingredient = FieldList(FormField(IngredientForm),min_entries=6)
    glassware = StringField("Glassware")
    garnish = StringField("Garnish")
    directions = TextAreaField("Directions")
    submit = SubmitField("Submit")

class CocktailForm(Form):
    name = StringField("name")
    # ingredients = FieldList(StringField('Liqour'))
    #
    # ounces = FieldList(StringField('Pour Ounce'))
    ingredient1 = StringField("Ingredient #1")
    ingredient2 = StringField("Ingredient_2")
    ingredient3 = StringField("Ingredient3")
    ingredient4 = StringField("Ingredient4")
    ingredient5 = StringField("Ingredient5")
    ingredient6 = StringField("Ingredient6")
    ounce1 = StringField("ounce1")
    ounce2 = StringField("ounce2")
    ounce3 = StringField("ounce3")
    ounce4 = StringField("ounce4")
    ounce5 = StringField("ounce5")
    ounce6 = StringField("ounce6")
    glassware = StringField("Glassware")
    garnish = StringField("Garnish")
    directions = TextAreaField("Directions")
    submit = SubmitField("Submit")
