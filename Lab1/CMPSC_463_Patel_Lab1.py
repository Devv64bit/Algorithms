companies_rankings = {
    'Google': ['Lisa', 'Tom', 'Sarah', 'Bob', 'Jane'],
    'Amazon': ['Sarah', 'Tom', 'Jane', 'Lisa', 'Bob'],
    'Meta': ['Jane', 'Lisa', 'Bob', 'Tom', 'Sarah'],
    'Apple': ['Jane', 'Bob', 'Tom', 'Sarah', 'Lisa'],
    'Microsoft': ['Bob', 'Tom', 'Sarah', 'Lisa', 'Jane']
}

employees_rankings = {
    'Lisa': ['Apple', 'Amazon', 'Google', 'Meta', 'Microsoft'],
    'Sarah': ['Amazon', 'Apple', 'Meta', 'Google', 'Microsoft'],
    'Bob': ['Microsoft', 'Meta', 'Google', 'Apple', 'Amazon'],
    'Tom': ['Meta', 'Google', 'Apple', 'Amazon', 'Microsoft'],
    'Jane': ['Apple', 'Google', 'Amazon', 'Microsoft', 'Meta']
}

# Keep track of people and companies that will end up together
matches = []

# Keep track of employee or comapnies who might not have matched yet.
available_employees = []
available_companies = []


def init_available_companies():
    for companies in companies_rankings:
        available_companies.append(companies)


def init_available_employees():
    for employees in employees_rankings:
        available_employees.append(employees)


def company_matching(companies):
    print("DEALING WITH %s" % (companies))
    for employees in companies_rankings[companies]:
        taken = [match for match in matches if employees in match]

        if (len(taken) == 0):
            matches.append([companies, employees])
            available_companies.remove(companies)
            print('%s is no longer available company and matched with %s' %
                  (companies, employees))
            break

        elif (len(taken) > 0):
            print('%s is taken already..' % (employees))
            current_company = employees_rankings[employees].index(taken[0][0])
            potential_company = employees_rankings[employees].index(companies)

            if (current_company < potential_company):
                print('Satisfied with %s..' % (taken[0][0]))
            else:
                print('%s is better than %s' % (companies, taken[0][0]))
                print('Releasing %s.. and matching %s and %s' %
                      (taken[0][0], companies, employees))

                available_companies.remove(companies)
                available_companies.append(taken[0][0])

                # Update the new match
                taken[0][0] = companies
                break


def employee_matching(employees):
    print("DEALING WITH %s" % (employees))
    for companies in employees_rankings[employees]:
        taken = [match for match in matches if companies in match]

        if (len(taken) == 0):
            matches.append([employees, companies])
            available_employees.remove(employees)
            print('%s is no longer available employee and matched with %s' %
                  (employees, companies))
            break

        elif (len(taken) > 0):
            print('%s is taken already..' % (companies))
            current_employee = companies_rankings[companies].index(taken[0][0])
            potential_employee = companies_rankings[companies].index(employees)

            if (current_employee < potential_employee):
                print('Satisfied with %s..' % (taken[0][0]))
            else:
                print('%s is better than %s' % (employees, taken[0][0]))
                print('Releasing %s.. and matching %s and %s' %
                      (taken[0][0], employees, companies))

                available_employees.remove(employees)
                available_employees.append(taken[0][0])

                # Update the new match
                taken[0][0] = employees
                break


def companies_stable_matching():
    while (len(available_companies) > 0):
        for companies in available_companies:
            company_matching(companies)


def employees_stable_matchings():
    while (len(available_employees) > 0):
        for employees in available_employees:
            employee_matching(employees)


# Company is the proposer

init_available_companies()
print(available_companies)
companies_stable_matching()
print(matches)


# Employee is the proposer
'''
init_available_employees()
print(available_employees)
employees_stable_matchings()
print(matches)
'''
