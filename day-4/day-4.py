import re

EYE_COLOR = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
HCL_REGEX = '^#[a-f0-9]{6}$'
PID_REGEX = '^[0-9]{9}$'
hcl_pattern = re.compile(HCL_REGEX)
pid_pattern = re.compile(PID_REGEX)
input_file = open("day-4.txt", "r")


def validate_passport_field(field, value):
    if field == 'byr':
        if 1920 <= int(value) <= 2002:
            return True;
    elif field == 'iyr':
        if 2010 <= int(value) <= 2020:
            return True;
    elif field == 'eyr':
        if 2020 <= int(value) <= 2030:
            return True;
    elif field == 'hgt':
        metric = value[-2 : ]
        if metric == 'cm':
            if 150 <= int(value[ : -2]) <= 193:
                return True
        else:
            if value[ : -2]:        
                if 59 <= int(value[ : -2]) <= 76:
                    return True
    elif field == 'hcl':
        if hcl_pattern.match(value):
            return True
    elif field == 'ecl':
        if value in EYE_COLOR:
            return True
    elif field == 'pid':
        if pid_pattern.match(value):
            return True
    else:
        return True
    print(field, value)
    return False

def check_batch(batch):
    passport_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
    passport_data = batch.split(' ')

    for data in passport_data:
        data = data.split(':')
        if not validate_passport_field(data[0], data[1]):
            print(batch)
            print()
            return False
        passport_fields.remove(data[0])
    if len(passport_fields) == 0 or (len(passport_fields) == 1 and 'cid' in passport_fields):
        # print(batch, passport_fields)
        return True
    return False
    

valid_passports = 0
invalid_passports = 0
batch = ''
for line in input_file:
    line = line.strip()
    if line != '':
        batch = batch + ' ' + line
    else:
        batch = batch.strip()
        if check_batch(batch):
            valid_passports += 1
        else:
            invalid_passports += 1
        batch = ''
batch = batch.strip()
if check_batch(batch):
    valid_passports += 1
else:
    invalid_passports += 1



print(valid_passports, invalid_passports)
