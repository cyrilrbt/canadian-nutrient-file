import os
import csv
import time
from flask_script import Command, Option
from cnf.settings import ROOT_PATH


class Import(Command):
    option_list = (
        Option('--source', '-s', dest='source'),
        Option('--batch', '-b', dest='batch', default=1000),

    )

    def csv(self, filename):
        _f = open(os.path.join(self.data_path, filename, ), 'r', encoding='iso8859')
        r = csv.reader(_f)
        next(r)
        return r

    def load_data(self, iterable, model, field_map, batch=1000):
        total = 0
        pending = []
        for items in iterable:
            items = [x for x in items if x]
            if items:
                pending.append(model(**dict(zip(field_map, items))))
                total += 1
                if len(pending) >= batch:
                    model.objects.insert(pending)
                    pending = []
        if pending:
            model.objects.insert(pending)
        return total

    def run(self, source, batch):
        batch = int(batch)
        self.data_path = source
        from flask import current_app as app
        with app.app_context():
            from cnf.models import (
                CNFFoodGroup, CNFFoodSource, CNFFoodName, CNFNutrientAmount,
                CNFNutrientName, CNFNutrientSource, CNFRefuseAmount, CNFRefuseName,
                CNFYieldAmount, CNFYieldName, CNFConversionFactor, CNFMeasureName
            )
        # I'll make this pep8 some day, maybe :)
        STEPS = (
            ('FOOD GROUP.csv', CNFFoodGroup, ('id', 'code', 'name', 'name_f')),
            ('FOOD SOURCE.csv', CNFFoodSource, ('id', 'code', 'description', 'description_f')),
            ('FOOD NAME.csv', CNFFoodName, ('id', 'code', 'food_group', 'food_source', 'description', 'description_f', 'date_of_entry', 'date_of_publication', 'country_code', 'scientific_name')),
            ('NUTRIENT AMOUNT.csv', CNFNutrientAmount, ('food', 'nutrient_name', 'nutrient_value', 'standard_error', 'number_of_observations', 'nutrient_source', 'date_of_entry')),
            ('NUTRIENT NAME.csv', CNFNutrientName, ('id', 'nutrient_code', 'nutrient_symbol', 'unit', 'name', 'name_f', 'tagname', 'nutrient_decimals')),
            ('NUTRIENT SOURCE.csv', CNFNutrientSource, ('id', 'code', 'description', 'description_f')),
            ('CONVERSION FACTOR.csv', CNFConversionFactor, ('food', 'measure', 'value', 'date_of_entry')),
            ('MEASURE NAME.csv', CNFMeasureName, ('id', 'name', 'name_f')),
            ('REFUSE AMOUNT.csv', CNFRefuseAmount, ('food', 'refuse_name', 'amount', 'date_of_entry')),
            ('REFUSE NAME.csv', CNFRefuseName, ('id', 'name', 'name_f')),
            ('YIELD AMOUNT.csv', CNFYieldAmount, ('food', 'yield_name', 'amount')),
            ('YIELD NAME.csv', CNFYieldName, ('id', 'name', 'name_f')),
        )
        for filename, model, fields in STEPS:
            print('Importing', filename)
            # TODO Dropping everything probably should be an option
            #      Not sure what to expect when you don't though
            print('  Dropping all items')
            model.objects.all().delete()
            s = time.time()
            cf = self.csv(filename)
            count = self.load_data(cf, model, fields, batch=batch)
            d = time.time() - s
            print(' ', count, 'rows imported in %.04fs\n' % d)
