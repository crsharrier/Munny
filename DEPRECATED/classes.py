from datetime import date, timedelta

class Bill:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name



class Period(Bill):

    all_periods = []

    def __init__(self, start, stop, fee):
        self.start = start
        self.stop = stop      
        self.fee = fee
        self.range = stop - start
        self.no_change = True

        self.boundaries = []
        self.all_periods.append(self)

    def __str__(self):
        return f"Period from {self.start.strftime('%d %b %Y')} to {self.end.strftime('%d %b %Y')}"
    
    @property
    def dates(self):
        return (self.start.strftime('%d %b %Y'), self.stop.strftime('%d %b %Y'))
    
    @property
    def length(self):
        return (self.stop - self.start).days
    
    @property
    def fully(self):
        fully = []
        for p in self.all_periods:
            for t in Tenant.all_tenants:
                if p.fully_present(t) == True:
                    p.fully.append(t)
        return fully
    
    @property
    def partially(self):
        partially = []
        for p in self.all_periods:
            for t in Tenant.all_tenants:
                if p.partially_present(t) == True:
                    p.partially.append(t)
                    p.no_change = False
        return partially

    #return True if given tenant is present for the full period
    def fully_present(self, tenant):
        if tenant.start <= self.start and tenant.stop >= self.stop:
            return True
        return False
    
    #return True if given tenant is present for part of the period but NOT for the full period
    def partially_present(self, tenant):
        if self.fully_present(tenant) == False:
            if (tenant.start <= self.stop and tenant.start >= self.start) or (tenant.stop >= self.start and tenant.stop <= self.stop):
                return True
        return False
        
    
    #calculate fee per person for a period with no_change
    def calculate_per_person(self):
        return self.fee / len(self.fully)
    
    
    def boundary_exists(self, b):
        bplus = b + timedelta(days=1)
        bminus = b - timedelta(days=1)
        if b in self.boundaries or bplus in self.boundaries or bminus in self.boundaries:
            return True
        return False
    
    #define function to deal with overlap periods
    def calculate_overlap_period(self):
        #set boundaries for sub_periods
        
        for t in self.partially:
            for date in (t.start, t.end):
                if date >= self.start and date <= self.end and not self.boundary_exists(date):
                    self.boundaries.append(date)
        self.boundaries.append(self.start)
        self.boundaries.append(self.end)
        self.boundaries.sort()

        #split into smaller periods - add new_fee to relevant tenants
        for i in range(0, len(self.boundaries) - 1):
            new_start = self.boundaries[i]
            new_stop = self.boundaries[i + 1]
            new_len = (new_stop - new_start).days
            new_fee = (new_len / self.length) * self.fee
            sub_p = Period(new_start, new_stop, new_fee)

            for t in super().all_tenants:
                if sub_p.fully_present(t) == True:
                    sub_p.fully.append(t)
                if sub_p.partially_present(t) == True:
                    sub_p.partially.append(t)
                    sub_p.no_change = False
            if sub_p.no_change:
                for t in sub_p.fully:
                    t.owes += sub_p.calculate_per_person()

class Tenant(Bill):

    all_tenants = []

    def __init__(self, name, start, stop=date.today()):
        self.name = name
        self.start = start
        self.stop = stop
        self.owes = 0
        self.all_tenants.append(self)

    def __str__(self):
        return self.name
    
    @property
    def dates(self):
        return (self.start.strftime('%d %b %Y'), self.end.strftime('%d %b %Y'))
    
    @property
    def length(self):
        return (self.stop - self.start).days