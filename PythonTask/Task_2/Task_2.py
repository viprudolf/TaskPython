class InsertAtmData:
    def __init__(self, base_distance, inserted_atms_count):
        self._base_distance = base_distance
        self._inserted_atms_count = inserted_atms_count

    @property
    def distance(self):
        return round(self._base_distance / self._inserted_atms_count, 2 )

    @property
    def inserted_atms_count(self):
        return self._inserted_atms_count

    def add_atm(self):
        self._inserted_atms_count += 1


def calculate(atms_count, new_added_atms, distances):
    insert_atm_datas = [InsertAtmData(distance, 1) for distance in distances]

    while new_added_atms > 0:
        atm_with_max_distance = max(insert_atm_datas, key=lambda data: data.distance)
        atm_with_max_distance.add_atm()
        new_added_atms -= 1

    output_distances = []

    for atms in insert_atm_datas:
        distance = atms.distance
        output_distances.extend([distance] * atms.inserted_atms_count)

    return output_distances
