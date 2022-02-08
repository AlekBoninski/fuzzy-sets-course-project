import numpy as np

from membership_functions import purchase_price, maintenance_price, doors, persons, luggage_space, safety


class VehicleCompositionGenerator:
    PURCHASE_PRICE = 0
    MAINTENANCE_PRICE = 1
    DOORS = 2
    PERSONS = 3
    LUGGAGE_SPACE = 4
    SAFETY = 5
    ACCEPTABILITY = 6

    PURCHASE_PRICE_LOW = 0
    PURCHASE_PRICE_MED = 1
    PURCHASE_PRICE_HIGH = 2
    PURCHASE_PRICE_VHIGH = 3

    MAINTENANCE_PRICE_LOW = 0
    MAINTENANCE_PRICE_MED = 1
    MAINTENANCE_PRICE_HIGH = 2
    MAINTENANCE_PRICE_VHIGH = 3

    DOORS_TWO = 0
    DOORS_THREE = 1
    DOORS_FOUR = 2
    DOORS_FIVE_MORE = 3

    PERSONS_TWO = 0
    PERSONS_FOUR = 1
    PERSONS_MORE = 2

    LUGGAGE_SPACE_SMALL = 0
    LUGGAGE_SPACE_MED = 1
    LUGGAGE_SPACE_BIG = 2

    SAFETY_LOW = 0
    SAFETY_MED = 1
    SAFETY_HIGH = 2

    ACCEPTABILITY_UNACC = 0
    ACCEPTABILITY_ACC = 1
    ACCEPTABILITY_GOOD = 2
    ACCEPTABILITY_VGOOD = 3

    def __init__(self, data_file):
        self.data_file = data_file
        self.purchase_price_acceptability_relation = np.zeros((4, 4), dtype=np.float16)
        self.maintenance_price_acceptability_relation = np.zeros((4, 4), dtype=np.float16)
        self.doors_acceptability_relation = np.zeros((4, 4), dtype=np.float16)
        self.persons_acceptability_relation = np.zeros((3, 4), dtype=np.float16)
        self.luggage_space_acceptability_relation = np.zeros((3, 4), dtype=np.float16)
        self.safety_acceptability_relation = np.zeros((3, 4), dtype=np.float16)
        self.__load_data()

    def __load_data(self):
        with open(self.data_file) as data_file:
            lines = data_file.readlines()
            for line in lines:
                line_data = line.strip().split(',')
                purchase_price = self.__get_purchase_price_index(line_data[self.PURCHASE_PRICE])
                maintenance_price = self.__get_maintenance_price_index(line_data[self.MAINTENANCE_PRICE])
                doors = self.__get_doors_index(line_data[self.DOORS])
                persons = self.__get_persons_index(line_data[self.PERSONS])
                luggage_space = self.__get_luggge_space_index(line_data[self.LUGGAGE_SPACE])
                safety = self.__get_safety_index(line_data[self.SAFETY])
                acceptability = self.__get_acceptability_inex(line_data[self.ACCEPTABILITY])

                self.purchase_price_acceptability_relation[purchase_price, acceptability] += 1
                self.maintenance_price_acceptability_relation[maintenance_price, acceptability] += 1
                self.doors_acceptability_relation[doors, acceptability] += 1
                self.persons_acceptability_relation[persons, acceptability] += 1
                self.luggage_space_acceptability_relation[luggage_space, acceptability] += 1
                self.safety_acceptability_relation[safety, acceptability] += 1

        self.__normalize_relations()

    def __normalize_relations(self):
        self.purchase_price_acceptability_relation = \
            self.purchase_price_acceptability_relation / self.purchase_price_acceptability_relation.sum(axis=1, keepdims=True)
        self.maintenance_price_acceptability_relation = \
            self.maintenance_price_acceptability_relation / self.maintenance_price_acceptability_relation.sum(axis=1, keepdims=True)
        self.doors_acceptability_relation = \
            self.doors_acceptability_relation / self.doors_acceptability_relation.sum(axis=1, keepdims=True)
        self.persons_acceptability_relation = \
            self.persons_acceptability_relation / self.persons_acceptability_relation.sum(axis=1, keepdims=True)
        self.luggage_space_acceptability_relation = \
            self.luggage_space_acceptability_relation / self.luggage_space_acceptability_relation.sum(axis=1, keepdims=True)
        self.safety_acceptability_relation = \
            self.safety_acceptability_relation / self.safety_acceptability_relation.sum(axis=1, keepdims=True)

    def __get_purchase_price_index(self, purchase_price):
        if purchase_price == 'vhigh':
            return self.PURCHASE_PRICE_VHIGH
        if purchase_price == 'high':
            return self.PURCHASE_PRICE_HIGH
        if purchase_price == 'med':
            return self.PURCHASE_PRICE_MED
        if purchase_price == 'low':
            return self.PURCHASE_PRICE_LOW

    def __get_maintenance_price_index(self, maintenance_price):
        if maintenance_price == 'vhigh':
            return self.MAINTENANCE_PRICE_VHIGH
        if maintenance_price == 'high':
            return self.MAINTENANCE_PRICE_HIGH
        if maintenance_price == 'med':
            return self.MAINTENANCE_PRICE_MED
        if maintenance_price == 'low':
            return self.MAINTENANCE_PRICE_LOW

    def __get_doors_index(self, doors):
        if doors == '2':
            return self.DOORS_TWO
        if doors == '3':
            return self.DOORS_THREE
        if doors == '4':
            return self.DOORS_FOUR
        if doors == '5more':
            return self.DOORS_FIVE_MORE

    def __get_persons_index(self, persons):
        if persons == '2':
            return self.PERSONS_TWO
        if persons == '4':
            return self.PERSONS_FOUR
        if persons == 'more':
            return self.PERSONS_MORE

    def __get_luggge_space_index(self, luggage_space):
        if luggage_space == 'small':
            return self.LUGGAGE_SPACE_SMALL
        if luggage_space == 'med':
            return self.LUGGAGE_SPACE_MED
        if luggage_space == 'big':
            return self.LUGGAGE_SPACE_BIG

    def __get_safety_index(self, safety):
        if safety == 'low':
            return self.SAFETY_LOW
        if safety == 'med':
            return self.SAFETY_MED
        if safety == 'high':
            return self.SAFETY_HIGH

    def __get_acceptability_inex(self, acceptability):
        if acceptability == 'unacc':
            return self.ACCEPTABILITY_UNACC
        if acceptability == 'acc':
            return self.ACCEPTABILITY_ACC
        if acceptability == 'good':
            return self.ACCEPTABILITY_GOOD
        if acceptability == 'vgood':
            return self.ACCEPTABILITY_VGOOD

    def for_vehicle_parameters(self, parameters):
        purchase_prices = parameters[:, self.PURCHASE_PRICE]
        maintenance_prices = parameters[:, self.MAINTENANCE_PRICE]
        num_doors = parameters[:, self.DOORS]
        num_persons = parameters[:, self.PERSONS]
        luggage_spaces = parameters[:, self.LUGGAGE_SPACE]
        safeties = parameters[:, self.SAFETY]

        self.purchase_price_relation = np.array([
            [purchase_price.f_low(price),
             purchase_price.f_med(price),
             purchase_price.f_high(price),
             purchase_price.f_vhigh(price)] for price in purchase_prices])
        self.maintenance_price_relation = np.array([
            [maintenance_price.f_low(price),
             maintenance_price.f_med(price),
             maintenance_price.f_high(price),
             maintenance_price.f_vhigh(price)] for price in maintenance_prices])
        self.doors_relation = np.array([
            [doors.f_two(d),
             doors.f_three(d),
             doors.f_four(d),
             doors.f_five_more(d)] for d in num_doors])
        self.persons_relation = np.array([
            [persons.f_two(p),
             persons.f_four(p),
             persons.f_more(p)] for p in num_persons])
        self.luggage_space_relation = np.array([
            [luggage_space.f_small(ls),
             luggage_space.f_med(ls),
             luggage_space.f_big(ls)] for ls in luggage_spaces])
        self.safety_relation = np.array([
            [safety.f_low(s),
             safety.f_med(s),
             safety.f_high(s)] for s in safeties])

        return self

    def min_max_composition(self):
        purchase_price_composition = self.__min_max(self.purchase_price_relation,
                                                    self.purchase_price_acceptability_relation)
        maintenance_price_composition = self.__min_max(self.maintenance_price_relation,
                                                       self.maintenance_price_acceptability_relation)
        doors_composition = self.__min_max(self.doors_relation, self.doors_acceptability_relation)
        persons_composition = self.__min_max(self.persons_relation,
                                             self.persons_acceptability_relation)
        luggage_space_composition = self.__min_max(self.luggage_space_relation,
                                                   self.luggage_space_acceptability_relation)
        safety_composition = self.__min_max(self.safety_relation,
                                            self.safety_acceptability_relation)
        return np.array([
            purchase_price_composition,
            maintenance_price_composition,
            doors_composition,
            persons_composition,
            luggage_space_composition,
            safety_composition
        ])

    def max_min_composition(self):
        purchase_price_composition = self.__max_min(self.purchase_price_relation, self.purchase_price_acceptability_relation)
        maintenance_price_composition = self.__max_min(self.maintenance_price_relation, self.maintenance_price_acceptability_relation)
        doors_composition = self.__max_min(self.doors_relation, self.doors_acceptability_relation)
        persons_composition = self.__max_min(self.persons_relation, self.persons_acceptability_relation)
        luggage_space_composition = self.__max_min(self.luggage_space_relation, self.luggage_space_acceptability_relation)
        safety_composition = self.__max_min(self.safety_relation, self.safety_acceptability_relation)
        return np.array([
            purchase_price_composition,
            maintenance_price_composition,
            doors_composition,
            persons_composition,
            luggage_space_composition,
            safety_composition
        ])

    def __max_min(self, matrix_a, matrix_b):
        rows, _ = matrix_a.shape
        _, cols = matrix_b.shape
        result = np.zeros((rows, cols))

        for row_index, row in enumerate(matrix_a):
            for col_index, col in enumerate(matrix_b.T):
                cell = max([min(*i) for i in zip(row, col)])
                result[row_index, col_index] = cell

        return result

    def __min_max(self, matrix_a, matrix_b):
        rows, _ = matrix_a.shape
        _, cols = matrix_b.shape
        result = np.zeros((rows, cols))

        for row_index, row in enumerate(matrix_a):
            for col_index, col in enumerate(matrix_b.T):
                cell = min([max(*i) for i in zip(row, col)])
                result[row_index, col_index] = cell

        return result

vehicle_params = np.array([
    [12_500, 100, 5, 6, 600, 5],
    [25_000, 250, 4, 4, 400, 4],
    # [55_000, 370, 2, 2, 370, 5],
    # [50_000, 200, 5, 6, 600, 5],
    # [130_000, 700, 4, 5, 550, 5],
    # [250_000, 1500, 2, 2, 150, 5]
])

res_max_min = VehicleCompositionGenerator('data/car.data')\
    .for_vehicle_parameters(vehicle_params)\
    .max_min_composition()

res_min_max = VehicleCompositionGenerator('data/car.data')\
    .for_vehicle_parameters(vehicle_params)\
    .min_max_composition()

print(res_max_min)
