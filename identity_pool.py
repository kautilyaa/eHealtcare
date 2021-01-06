from uuid import uuid4
from collections import OrderedDict
from id import Identity

class Identity_Pool (object):#used to assign as well as cap the number of patients
    def __init__(self, number_of_Identities):
        self.Identities = [Identity(self) for x in xrange(number_of_Identities)] 
        self.id_assignments = OrderedDict() 

    def get_id_count(self):
        return len(self.Identities) 
        
    def assign_id(self, patient):
        if self.get_id_count() > 0:
            self.id_assignments[patient.get_patient_id()] = self.Identities.pop() #Assign a device from the list of device objects.
        else:
            raise Exception("No Identities left to assign!")
           

    def return_device(self, patient, id):
        self.Identities.append(id)
        if self.id_assignments.has_key(patient.get_patient_id()):
            del self.id_assignments[patient.get_patient_id()] 
        else:
            pass