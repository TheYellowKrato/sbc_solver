class FormationsParser:
    positions_data = [{"uniqueId": 0, "typeId": 0, "uniqueName": "GK", "typeName": "GK"},
                      {"uniqueId": 1, "typeId": 1, "uniqueName": "SW", "typeName": "N/A"},
                      {"uniqueId": 2, "typeId": 2, "uniqueName": "RWB", "typeName": "RWB"},
                      {"uniqueId": 3, "typeId": 3, "uniqueName": "RB", "typeName": "RB"},
                      {"uniqueId": 4, "typeId": 5, "uniqueName": "RCB", "typeName": "CB"},
                      {"uniqueId": 5, "typeId": 5, "uniqueName": "CB", "typeName": "CB"},
                      {"uniqueId": 6, "typeId": 5, "uniqueName": "LCB", "typeName": "CB"},
                      {"uniqueId": 7, "typeId": 7, "uniqueName": "LB", "typeName": "LB"},
                      {"uniqueId": 8, "typeId": 8, "uniqueName": "LWB", "typeName": "LWB"},
                      {"uniqueId": 9, "typeId": 10, "uniqueName": "RDM", "typeName": "CDM"},
                      {"uniqueId": 10, "typeId": 10, "uniqueName": "CDM", "typeName": "CDM"},
                      {"uniqueId": 11, "typeId": 10, "uniqueName": "LDM", "typeName": "CDM"},
                      {"uniqueId": 12, "typeId": 12, "uniqueName": "RM", "typeName": "RM"},
                      {"uniqueId": 13, "typeId": 14, "uniqueName": "RCM", "typeName": "CM"},
                      {"uniqueId": 14, "typeId": 14, "uniqueName": "CM", "typeName": "CM"},
                      {"uniqueId": 15, "typeId": 14, "uniqueName": "LCM", "typeName": "CM"},
                      {"uniqueId": 16, "typeId": 16, "uniqueName": "LM", "typeName": "LM"},
                      {"uniqueId": 17, "typeId": 18, "uniqueName": "RAM", "typeName": "CAM"},
                      {"uniqueId": 18, "typeId": 18, "uniqueName": "CAM", "typeName": "CAM"},
                      {"uniqueId": 19, "typeId": 18, "uniqueName": "LAM", "typeName": "CAM"},
                      {"uniqueId": 20, "typeId": 20, "uniqueName": "RF", "typeName": "RF"},
                      {"uniqueId": 21, "typeId": 21, "uniqueName": "CF", "typeName": "CF"},
                      {"uniqueId": 22, "typeId": 22, "uniqueName": "LF", "typeName": "LF"},
                      {"uniqueId": 23, "typeId": 23, "uniqueName": "RW", "typeName": "RW"},
                      {"uniqueId": 24, "typeId": 25, "uniqueName": "RS", "typeName": "ST"},
                      {"uniqueId": 25, "typeId": 25, "uniqueName": "ST", "typeName": "ST"},
                      {"uniqueId": 26, "typeId": 25, "uniqueName": "LS", "typeName": "ST"},
                      {"uniqueId": 27, "typeId": 27, "uniqueName": "LW", "typeName": "LW"}]
    formations_data = [
        {"id": 22, "index": 0, "name": "f3142", "generalPositionSlots": [0, 5, 5, 5, 10, 12, 14, 14, 16, 25, 25],
         "uniquePositionSlots": [0, 4, 5, 6, 10, 12, 13, 15, 16, 24, 26]},
        {"id": 23, "index": 1, "name": "f3412", "generalPositionSlots": [0, 5, 5, 5, 12, 14, 14, 16, 18, 25, 25],
         "uniquePositionSlots": [0, 4, 5, 6, 12, 13, 15, 16, 18, 24, 26]},
        {"id": 24, "index": 2, "name": "f3421", "generalPositionSlots": [0, 5, 5, 5, 12, 14, 14, 16, 20, 22, 25],
         "uniquePositionSlots": [0, 4, 5, 6, 12, 13, 15, 16, 20, 22, 25]},
        {"id": 25, "index": 3, "name": "f343", "generalPositionSlots": [0, 5, 5, 5, 12, 14, 14, 16, 23, 25, 27],
         "uniquePositionSlots": [0, 4, 5, 6, 12, 13, 15, 16, 23, 25, 27]},
        {"id": 27, "index": 4, "name": "f352", "generalPositionSlots": [0, 5, 5, 5, 10, 10, 12, 16, 18, 25, 25],
         "uniquePositionSlots": [0, 4, 5, 6, 9, 11, 12, 16, 18, 24, 26]},
        {"id": 14, "index": 5, "name": "f41212", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 12, 16, 18, 25, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 10, 12, 16, 18, 24, 26]},
        {"id": 15, "index": 6, "name": "f41212a", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 14, 14, 18, 25, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 10, 13, 15, 18, 24, 26]},
        {"id": 1, "index": 7, "name": "f4132", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 12, 14, 16, 25, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 10, 12, 14, 16, 24, 26]},
        {"id": 2, "index": 8, "name": "f4141", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 12, 14, 14, 16, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 10, 12, 13, 15, 16, 25]},
        {"id": 13, "index": 9, "name": "f4222", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 10, 18, 18, 25, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 9, 11, 17, 19, 24, 26]},
        {"id": 3, "index": 10, "name": "f4231", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 10, 18, 18, 18, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 9, 11, 17, 18, 19, 25]},
        {"id": 4, "index": 11, "name": "f4231a", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 10, 12, 16, 18, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 9, 11, 12, 16, 18, 25]},
        {"id": 5, "index": 12, "name": "f424", "generalPositionSlots": [0, 3, 5, 5, 7, 14, 14, 23, 25, 25, 27],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 13, 15, 23, 24, 26, 27]},
        {"id": 6, "index": 13, "name": "f4312", "generalPositionSlots": [0, 3, 5, 5, 7, 14, 14, 14, 18, 25, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 13, 14, 15, 18, 24, 26]},
        {"id": 7, "index": 14, "name": "f4321", "generalPositionSlots": [0, 3, 5, 5, 7, 14, 14, 14, 20, 22, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 13, 14, 15, 20, 22, 25]},
        {"id": 8, "index": 15, "name": "f433", "generalPositionSlots": [0, 3, 5, 5, 7, 14, 14, 14, 23, 25, 27],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 13, 14, 15, 23, 25, 27]},
        {"id": 9, "index": 16, "name": "f433a", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 14, 14, 23, 25, 27],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 10, 13, 15, 23, 25, 27]},
        {"id": 10, "index": 17, "name": "f433b", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 10, 14, 23, 25, 27],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 9, 11, 14, 23, 25, 27]},
        {"id": 11, "index": 18, "name": "f433c", "generalPositionSlots": [0, 3, 5, 5, 7, 14, 14, 18, 23, 25, 27],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 13, 15, 18, 23, 25, 27]},
        {"id": 12, "index": 19, "name": "f433d", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 14, 14, 21, 23, 27],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 10, 13, 15, 21, 23, 27]},
        {"id": 19, "index": 20, "name": "f4411", "generalPositionSlots": [0, 3, 5, 5, 7, 12, 14, 14, 16, 21, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 12, 13, 15, 16, 21, 25]},
        {"id": 18, "index": 21, "name": "f4411a", "generalPositionSlots": [0, 3, 5, 5, 7, 12, 14, 14, 16, 18, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 12, 13, 15, 16, 18, 25]},
        {"id": 16, "index": 22, "name": "f442", "generalPositionSlots": [0, 3, 5, 5, 7, 12, 14, 14, 16, 25, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 12, 13, 15, 16, 24, 26]},
        {"id": 17, "index": 23, "name": "f442a", "generalPositionSlots": [0, 3, 5, 5, 7, 10, 10, 12, 16, 25, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 9, 11, 12, 16, 24, 26]},
        {"id": 21, "index": 24, "name": "f451", "generalPositionSlots": [0, 3, 5, 5, 7, 12, 14, 16, 18, 18, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 12, 14, 16, 17, 19, 25]},
        {"id": 20, "index": 25, "name": "f451a", "generalPositionSlots": [0, 3, 5, 5, 7, 12, 14, 14, 14, 16, 25],
         "uniquePositionSlots": [0, 3, 4, 6, 7, 12, 13, 14, 15, 16, 25]},
        {"id": 29, "index": 26, "name": "f5212", "generalPositionSlots": [0, 2, 5, 5, 5, 8, 14, 14, 18, 25, 25],
         "uniquePositionSlots": [0, 2, 4, 5, 6, 8, 13, 15, 18, 24, 26]},
        {"id": 30, "index": 27, "name": "f5221", "generalPositionSlots": [0, 2, 5, 5, 5, 8, 14, 14, 23, 25, 27],
         "uniquePositionSlots": [0, 2, 4, 5, 6, 8, 13, 15, 23, 25, 27]},
        {"id": 31, "index": 28, "name": "f532", "generalPositionSlots": [0, 2, 5, 5, 5, 8, 14, 14, 14, 25, 25],
         "uniquePositionSlots": [0, 2, 4, 5, 6, 8, 13, 14, 15, 24, 26]},
        {"id": 33, "index": 29, "name": "f541a", "generalPositionSlots": [0, 2, 5, 5, 5, 8, 12, 14, 14, 16, 25],
         "uniquePositionSlots": [0, 2, 4, 5, 6, 8, 12, 13, 15, 16, 25]}]

    def identify_formation(self, target_formation):
        position_slots = []
        for formation in self.formations_data:
            if formation["name"] == target_formation:
                position_slots = formation["uniquePositionSlots"]
                break

        positions = []
        for position in position_slots:
            positions.append(self.positions_data[position])

        positions.reverse()

        return positions

    def find_uniqueId_from_name(self, name):
        for position in self.positions_data:
            if position["typeName"] == name:
                return position["uniqueId"]
