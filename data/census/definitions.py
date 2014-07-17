'''Census data import definitions'''

# State-level regions to load'''
STATES = ['ok', 'pa', 'ma', 'dc', 'va', 'md']

# Census 'tables' to load
# key is the name of the table
# value has the following key-value pairs:
#   description: Text description of table
#   valtype: 'decimal:5,2' if decimal point w/ 5 max digits and 2 decimal
#     points precision (0.00 to 100.00), else assumed integer
TABLES = {
    #'B01001': {
    #    'description': 'Sex By Age',
    #},
    #'B01002': {
    #    'description': 'Median Age By Sex',
    #    'valtype': 'decimal:5,2',
    #},
    'B01003': {
        'description': 'Total Population',
    },
    #'B02001': {
    #    'description': 'Race',
    #},
    #'B07003': {
    #    'description': (
    #        'Geographical Mobility In The Past Year By Sex For Current'
    #        ' Residence In The United States US Only'),
    #},
    'B07013': {
        'description': (
            'Geographical Mobility in the Past Year by Tenure'
            ' for Current Residence in the United States'),
    },
    #'B07413': {
    #    'description': (
    #        'Geographical Mobility in the Past Year by Tenure for Residence'
    #        ' 1 Year Ago in the United States'),
    #},
    #'B08006': {
    #    'description': 'Sex of Workers by Means of Transportation to Work',
    #},
    #'B08016': {
    #    'description': (
    #        'Place Of Work For Workers 16 Years And Over--Metropolitan'
    #        ' Statistical Area Level'),
    #},
    #'B08018': {
    #    'description': (
    #        'Place Of Work For Workers 16 Years And Over--Not Metropolitan'
    #        ' Or Micropolitan Statistical Area Level'),
    #},
    #'B08301': {
    #    'description': 'Means Of Transportation To Work',
    #},
    'B08303': {
        'description': 'Travel Time To Work',
    },
    'B09002': {
        'description': 'Own Children by Family Type and Age',
    },
    #'B10002': {
    #    'description': (
    #        'Grandchildren Living with a Grandparent Householder by'
    #        ' Grandparent Responsibility and Prence of Parent'),
    #},
    #'B11001': {
    #    'description': 'Household Type (Including Living Alone)',
    #},
    #'B11003': {
    #    'description': 'Family Type by Presense and Age of Own Children',
    #},
    #'B11004': {
    #    'description': 'Family Type by Presence and Age of Related Children',
    #},
    'B12001': {
        'description': 'Sex by Marital Status',
    },
    'B12503': {
        'description': (
            'Divorces In The Last Year By Sex By Marital Status For The'
            ' Population 15 Years And Over Nation and State Only'),
    },
    #'B13001': {
    #    'description': 'Marital Status By Age For Women 15 To 50 Years',
    #},
    #'B13002': {
    #    'description': (
    #        'Women 15 To 50 Years Who Had A Birth In The Past 12 Months By'
    #        ' Marital Status And Age'),
    #},
    #'B13004': {
    #    'description': (
    #        'Women 15 To 50 Years Who Had A Birth In The Past 12 Months By'
    #        ' Marital Status And Presence Of Unmarried Partner'),
    #},
    'B14001': {
        'description': (
            'School Enrollment By Level Of School For The Population 3 Years'
            ' And Over'),
    },
    #'B14002': {
    #    'description': (
    #        'Sex By School Enrollment By Level Of School By Type Of School'
    #        ' For The Population 3 Years And Over'),
    #},
    #'B14004': {
    #    'description': (
    #        'Sex By College Or Graduate School Enrollment By Type Of School'
    #        ' By Age For The Population 15 Years And Over'),
    #},
    #'B14007': {
    #    'description': (
    #        'School Enrollment By Detailed Level Of School For The Population'
    #        ' 3 Years And Over'),
    #},
    'B15002': {
        'description': (
            'Sex by Educational Attainment for the Population'
            ' 25 Years and Over')
    },
    #'C15002': {
    #    'description': 'Sex by Educational Attainment.',
    #},
    'B15003': {
        'description': (
            'Educational Attainment For The Population 25 Years And Over'),
    },
    'B17001': {
        'description': 'Poverty Status In The Past 12 Months By Sex By Age',
    },
    #'C17002': {
    #    'description': (
    #        'Ratio Of Income To Poverty Level In The Past 12 Months'),
    #},
    #'B17003': {
    #    'description': (
    #        'Poverty Status In The Past 12 Months Of Individuals By Sex By'
    #        ' Educational Attainment'),
    #},
    #'B17010': {
    #    'description': (
    #        'Poverty Status In The Past 12 Months Of Families By Family Type'
    #        ' By Presence Of Related Children Under 18 Years By Age Of'
    #        ' Related Children'),
    #},
    #'B18101': {
    #    'description': 'Sex By Age By Disability Status',
    #},
    #'B18135': {
    #    'description': (
    #        'Age By Disability Status By Health Insurance Coverage Status'),
    #},
    #'B19013': {
    #    'description': (
    #        'Median Household Income In The Past 12 Months'
    #        ' (In 2012 Inflation-Adjusted Dollars)'),
    #},
    #'B19055': {
    #    'description': (
    #        'Social Security Income In The Past 12 Months For Households'),
    #},
    #'B19056': {
    #    'description': (
    #        'Supplemental Security Income (Ssi) In The Past 12 Months For'
    #        ' Households'),
    #},
    #'B19057': {
    #    'description': (
    #        'Public Assistance Income In The Past 12 Months For Households'),
    #},
    'B19058': {
        'description': (
            'Public Assistance Income Or Food Stamps/Snap In The Past'
            ' 12 Months For Households'),
    },
    #'B19083': {
    #    'description': 'Gini Index Of Income Inequality',
    #    'valtype': 'decimal:5,2',
    #},
    #'B19113': {
    #    'description': (
    #        'Median Family Income In The Past 12 Months'
    #        ' (In 2012 Inflation-Adjusted Dollars)'),
    #},
    #'B19301': {
    #    'description': (
    #        'Per Capita Income In The Past 12 Months'
    #        ' (In 2012 Inflation-Adjusted Dollars)'),
    #},
    #'B22002': {
    #    'description': (
    #        'Receipt Of Food Stamps/Snap In The Past 12 Months By Presence'
    #        ' Of Children Under 18 Years By Household Type For Households'),
    #},
    #'B22003': {
    #    'description': (
    #        'Receipt Of Food Stamps/Snap In The Past 12 Months By Poverty'
    #        ' Status In The Past 12 Months For Households'),
    #},
    'B23001': {
        'description': (
            'Sex by Age by Employment Status for the Population 16 Years'
            ' and Over'),
    },
    #'B23020': {
    #    'description': (
    #        'Mean Usual Hours Worked In The Past 12 Months For Workers'
    #        ' 16 To 64 Years'),
    #    'valtype': 'decimal:5,2',
    #},
    #'B23025': {
    #    'description': (
    #        'Employment Status For The Population 16 Years And Over'),
    #},
    #'B25001': {
    #    'description': 'Housing Units',
    #},
    #'B25002': {
    #    'description': 'Occupancy Status',
    #},
    #'B25003': {
    #    'description': 'Tenure',
    #},
    #'B25004': {
    #    'description': 'Vacancy',
    #},
    'B25014': {
        'description': 'Tenure by Occupants Per Room',
    },
    #'B25016': {
    #    'description': 'Tenure by Plumbing Facilties by Occupants Per Room',
    #},
    #'B25027': {
    #    'description': 'Mortgage Status By Age Of Householder',
    #},
    #'B25034': {
    #    'description': 'Year Structure Built',
    #},
    #'B25035': {
    #    'description': 'Median Year Structure Built',
    #},
    #'B25042': {
    #    'description': 'Tenure by Bedrooms',
    #},
    'B25048': {
        'description': 'Plumbing Facilities for Occupied Housing Units',
    },
    'B25052': {
        'description': 'Kitchen Facilities for Occupied Housing Units',
    },
    #'B25058': {
    #    'description': 'Median Contract Rent (Dollars)',
    #},
    #'B25064': {
    #    'description': 'Median Gross Rent (Dollars)',
    #},
    'B25070': {
        'description': (
            'Gross Rent as a Percentage of Household Income in the Past'
            ' 12 Months'),
    },
    'B25075': {
        'description': 'Value',
    },
    #'B25087': {
    #    'description': 'Mortgage Status And Selected Monthly Owner Costs',
    #},
    'B25091': {
        'description': (
            'Mortgage Status by Selected Monthly Owner Costs as a Percentage'
            ' of Household Income in the Past 12 Months'),
    },
    #'B25106': {
    #    'description': (
    #        'Tenure by Housing Costs as a Percentage of Household Income'),
    #},
    #'B27001': {
    #    'description': 'Health Insurance Coverage Status by Sex by Age',
    #},
    #'B27002': {
    #    'description': 'Private Health Insurance Status By Sex By Age',
    #},
    #'B27003': {
    #    'description': 'Public Health Insurance Status By Sex By Age',
    #},
    'C27006': {
        'description': 'Medicare Coverage By Sex By Age',
    },
    #'C27007': {
    #    'description': 'Medicaid/Means-Tested Public Coverage By Sex By Age',
    #},
}
