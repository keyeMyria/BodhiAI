import numpy as np
import pickle
import math
from datetime import datetime, date
from .models import Subject
from more_itertools import unique_everseen
from QuestionsAndPapers.models import *
try:
    ptp = '/home/prashant/Desktop/programming/projects/bod/src/bodhialgorithms/'

    '''
    load pickles for data transformation and prediction (hindi)
    '''
    pickle_in_hindi = open('/home/prashant/Desktop/programming/projects/bod/src/bodhialgorithms/preprocesshindihy.pickle',
                           'rb')
    svm_pickle_hindi = open('/home/prashant/Desktop/programming/projects/bod/src/bodhialgorithms/svmhindihhy.pickle', 'rb')
    sca_hindi = pickle.load(pickle_in_hindi)
    svmhindihhy = pickle.load(svm_pickle_hindi)

    '''
    load pickles for data transformation and prediction (maths)
    '''
    pickle_in_maths = open(ptp + 'preprocesshindihy.pickle', 'rb')
    knn7_pickle_maths = open(ptp + 'svmhindihhy.pickle', 'rb')
    sca_maths = pickle.load(pickle_in_maths)
    knn7mathshhy = pickle.load(knn7_pickle_maths)

    '''
    load pickles for data transformation and prediction (english)
    '''
    pickle_in_english = open(ptp + 'preprocesshindihy.pickle', 'rb')
    knn7_pickle_english = open(ptp + 'svmhindihhy.pickle', 'rb')
    sca_english = pickle.load(pickle_in_english)
    knn7englishhhy = pickle.load(knn7_pickle_english)

    '''
    load pickles for data transformation and prediction (science)
    '''
    pickle_in_science = open(ptp + 'preprocesshindihy.pickle', 'rb')
    knn7_pickle_science = open(ptp + 'svmhindihhy.pickle', 'rb')
    sca_science = pickle.load(pickle_in_science)
    knn7sciencehhy = pickle.load(knn7_pickle_science)
except:
    pass

# test1,test2,test3,age,section
# x = np.array([[9, 10, 10, 12, 1]])
# x = sca.transform(x)
# print(x)
# prd = svmhindihhy.predict(x)
# print(prd)


def hindi_3testhyprediction(test1, test2, test3, DOB, section):
    '''
    convert test marks into numpy arrays
    '''
    t1 = int(test1)
    t2 = int(test2)
    t3 = int(test3)

    if section == 'a':
        section = 1
    elif section == 'b':
        section = 2

    '''
    calculate age using DOB (dd/mm/year)
    '''
    days_in_year = 365.2425
    age = int((date(2018, 4, 1) - DOB).days / days_in_year)
    # age = int((date.today() - DOB).days / days_in_year)

    overall = np.array([[t1, t2, t3, age, section]])

    '''
        transform(scale) data to original data of school
    '''
    overall = sca_hindi.transform(overall)
    '''
        predict the hy marks using the trained ml algorithm
    '''
    prediction = svmhindihhy.predict(overall)
    return prediction


def maths_3testhyprediction(test1, test2, test3, DOB, section):
    '''
    convert test marks into numpy arrays
    '''
    t1 = int(test1)
    t2 = int(test2)
    t3 = int(test3)

    if section == 'a':
        section = 1
    elif section == 'b':
        section = 2

    '''
        calculate age using DOB (dd/mm/year)
    '''
    days_in_year = 365.2425
    age = int((date(2018, 4, 1) - DOB).days / days_in_year)

    overall = np.array([[t1, t2, t3, age, section]])

    '''
        transform(scale) data to original data of school
    '''
    overall = sca_maths.transform(overall)
    '''
        predict the hy marks using the trained ml algorithm
    '''
    prediction = knn7mathshhy.predict(overall)
    return prediction


def english_3testhyprediction(test1, test2, test3, DOB, section):
    '''
    convert test marks into numpy arrays
    '''
    t1 = int(test1)
    t2 = int(test2)
    t3 = int(test3)

    if section == 'a':
        section = 1
    elif section == 'b':
        section = 2

    '''
        calculate age using DOB (dd/mm/year)
    '''
    days_in_year = 365.2425
    age = int((date(2018, 4, 1) - DOB).days / days_in_year)

    overall = np.array([[t1, t2, t3, age, section]])

    '''
        transform(scale) data to original data of school
    '''
    overall = sca_english.transform(overall)
    '''
        predict the hy marks using the trained ml algorithm
    '''
    prediction = knn7englishhhy.predict(overall)
    return prediction


def science_3testhyprediction(test1, test2, test3, DOB, section):
    '''
    convert test marks into numpy arrays
    '''
    t1 = int(test1)
    t2 = int(test2)
    t3 = int(test3)

    if section == 'a':
        section = 1
    elif section == 'b':
        section = 2

        '''
            calculate age using DOB (dd/mm/year)
        '''
    days_in_year = 365.2425

    age = int((date(2018, 4, 1) - DOB).days / days_in_year)

    overall = np.array([[t1, t2, t3, age, section]])

    '''
        transform(scale) data to original data of school
    '''
    overall = sca_science.transform(overall)
    '''
        predict the hy marks using the trained ml algorithm
    '''
    prediction = knn7sciencehhy.predict(overall)
    return prediction


def predictionConvertion(prediction):
    try:
        prediction = prediction[0]
    except:
        pass

    print(prediction)
    if prediction == 0:
        conversion = 35
    elif prediction == 1:
        conversion = 45
    elif prediction == 2:
        conversion = 55
    elif prediction == 3:
        conversion = 65
    elif prediction == 4:
        conversion = 75
    elif prediction == 5:
        conversion = 85
    elif prediction == 6:
        conversion = 95
    else:
        conversion = '404'
    return conversion


# function for updating all the half yearly predictions (whole database)


def update_all_predictedmarks():
    subject = Subject.objects.all()
    alluniquestudents = []
    alluniquestudents = list(unique_everseen(alluniquestudents))
    for i in subject:
        alluniquestudents.append(i.student)
    allsubjects = []
    for j in alluniquestudents:
        allsubjects.extend(j.subject_set.all())

    for thisSubject in allsubjects:
        if thisSubject.name == 'Hindi':
            cl = str(thisSubject.student.klass)
            if cl[-1] == 'a':
                section = 'a'
            else:
                section = 'b'
            thisSubject.predicted_hy = int(
                hindi_3testhyprediction(thisSubject.test1, thisSubject.test2, thisSubject.test3,
                                        thisSubject.student.dob, section))

            thisSubject.save()
        elif thisSubject.name == 'English':
            cl = str(thisSubject.student.klass)
            if cl[-1] == 'a':
                section = 'a'
            else:
                section = 'b'
            thisSubject.predicted_hy = int(
                english_3testhyprediction(thisSubject.test1, thisSubject.test2, thisSubject.test3,
                                          thisSubject.student.dob, section))
            thisSubject.save()

        elif thisSubject.name == 'Maths':
            cl = str(thisSubject.student.klass)
            if cl[-1] == 'a':
                section = 'a'
            else:
                section = 'b'
            thisSubject.predicted_hy = int(
                maths_3testhyprediction(thisSubject.test1, thisSubject.test2, thisSubject.test3,
                                        thisSubject.student.dob, section))
            thisSubject.save()

        elif thisSubject.name == 'Science':
            cl = str(thisSubject.student.klass)
            if cl[-1] == 'a':
                section = 'a'
            else:
                section = 'b'
            thisSubject.predicted_hy = int(
                science_3testhyprediction(thisSubject.test1, thisSubject.test2, thisSubject.test3,
                                          thisSubject.student.dob, section))
            thisSubject.save()

        else:
            pass


def get_predicted_marks(user, subjects):
    try:
        hindi = subjects.get(name='Hindi')
        predicted_hindihy = predictionConvertion(hindi.predicted_hy)
    except:
        predicted_hindihy = 0
    try:
        maths = subjects.get(name='Maths')
        predicted_mathshy = predictionConvertion(maths.predicted_hy)
    except:
        predicted_mathshy = 0
    try:
        english = subjects.get(name='English')
        predicted_englishhy = predictionConvertion(english.predicted_hy)
    except:
        predicted_englishhy = 0
    try:
        science = subjects.get(name='Science')
        predicted_sciencehy = predictionConvertion(science.predicted_hy)
    except:
        predicted_sciencehy = 0

    return predicted_hindihy, predicted_mathshy, predicted_englishhy, predicted_sciencehy


def averageoftest(test, test2=None, test3=None):
    if test2 is None and test3 is None:
        testmarks = np.array(test)
        return np.mean(testmarks)
    elif test3 is None:
        testmarks = np.array(test)
        testmarks2 = np.array(test2)
        return np.mean(testmarks), np.mean(testmarks2)
    else:
        testmarks = np.array(test)
        testmarks2 = np.array(test2)
        testmarks3 = np.array(test3)
        return np.mean(testmarks), np.mean(testmarks2), np.mean(testmarks3)


# all the helper functions for teacher pages

def teacher_get_students_classwise(req):
    user = req.user
    profile = user.teacher
    subject = profile.subject_set.all()

    allstudents = []  # list of subjects of all students (taught by the teacher)
    klass_dict = {}  # dictionary for subjects of individual classes
    all_klasses = []  # list of all unique classes taught by the teacher
    all_klasses = list(unique_everseen(all_klasses))

    for i in subject:
        allstudents.append(i)
        all_klasses.append(str(i.student.klass))

    # fill out the dictionary for subjects of each class
    for k in all_klasses:
        sub9a = []
        for j in subject:
            if str(j.student.klass) == str(k):
                sub9a.append(j)
                temp_dict = {str(k): sub9a}
                klass_dict.update(temp_dict)
    return klass_dict, all_klasses


def teacher_get_testmarks_classwise(req, klass_dict):
    klass_test1_dict = {}  # dictionary to hold test1 marks of different classes
    klass_test2_dict = {}
    klass_test3_dict = {}

    # fill out the above dictionaries

    for i in klass_dict.values():
        kk = i
        klasstest1 = []
        klasstest2 = []
        klasstest3 = []

        for j in kk:
            klasstest1.append(j.test1)
            klasstest2.append(j.test2)
            klasstest3.append(j.test3)
            testm1 = {str(j.student.klass): klasstest1}
            testm2 = {str(j.student.klass): klasstest2}
            testm3 = {str(j.student.klass): klasstest3}
        klass_test1_dict.update(testm1)
        klass_test2_dict.update(testm2)
        klass_test3_dict.update(testm3)
    return klass_test1_dict, klass_test2_dict, klass_test2_dict


def teacher_get_classwise_studnetNames(request, klass_dict):
    ktdict = {}
    for i in klass_dict.values():
        kk = i
        kt = []
        for k in kk:
            kt.append(k.student)
            stu1 = {str(k.student.klass): kt}
        ktdict.update(stu1)
    return ktdict


def teacher_get_classwise_listofStudents(request, studict):
    kl0 = []
    kl1 = []
    kl2 = []
    kl3 = []
    kl4 = []
    kl5 = []
    nine_a = []
    nine_b = []
    nine_c = []
    ten_a = []
    ten_b = []
    ten_c = []

    for i, n in enumerate(studict.values()):
        eval('kl' + str(i)).extend(n)
    for i in kl0:

        if str(i.klass) == '9th a':
            nine_a = kl0
            break

    for i in kl1:
        if str(i.klass) == '9th b':
            nine_b = kl1
            break
    return nine_a, nine_b


def teacher_listofStudents(profile, klass):
    listofstudents = []
    subject_list = profile.subject_set.filter(student__klass__name=klass)
    for i in subject_list:
        listofstudents.append(i)
    return listofstudents


def teacher_listofStudentsMarks(profile, which_class):
    marks_class_test1 = []
    marks_class_test2 = []
    marks_class_test3 = []
    marks_class_predictedHy = []
    sub_class = profile.subject_set.filter(student__klass__name=which_class)
    if not sub_class:
        pass
    else:
        for i in sub_class:
            if i.test1:
                marks_class_test1.append(i.test1)
            if i.test2:
                marks_class_test2.append(i.test2)
            if i.test3:
                marks_class_test3.append(i.test3)
            if i.predicted_hy:
                marks_class_predictedHy.append(i.predicted_hy)
    return marks_class_test1, marks_class_test2, marks_class_test3, marks_class_predictedHy


def find_grade_from_marks(test1, test2=None, test3=None):
    test1_grade = []
    test2_grade = []
    test3_grade = []
    test1 = np.array(test1)
    if test2 is None:
        for i, n in enumerate(test1):
            if n < 4:
                test1_grade.append('F')
            if 4 <= n < 5:
                test1_grade.append('E')
            if 5 <= n < 6:
                test1_grade.append('D')
            if 6 <= n < 7:
                test1_grade.append('C')
            if 7 <= n < 8:
                test1_grade.append('B')
            if 8 <= n < 9:
                test1_grade.append('A')
            if 9 <= n <= 10:
                test1_grade.append('S')
        return test1_grade
    elif test3 is None:

        test2 = np.array(test2)

        for i, n in enumerate(test1):
            if n < 4:
                test1_grade.append('F')
            if 4 <= n < 5:
                test1_grade.append('E')
            if 5 <= n < 6:
                test1_grade.append('D')
            if 6 <= n < 7:
                test1_grade.append('C')
            if 7 <= n < 8:
                test1_grade.append('B')
            if 8 <= n < 9:
                test1_grade.append('A')
            if 9 <= n <= 10:
                test1_grade.append('S')

        for i, n in enumerate(test2):
            if n < 4:
                test2_grade.append('F')
            if 4 <= n < 5:
                test2_grade.append('E')
            if 5 <= n < 6:
                test2_grade.append('D')
            if 6 <= n < 7:
                test2_grade.append('C')
            if 7 <= n < 8:
                test2_grade.append('B')
            if 8 <= n < 9:
                test2_grade.append('A')
            if 9 <= n <= 10:
                test2_grade.append('S')
        return test1_grade, test2_grade
    else:
        test2 = np.array(test2)
        test3 = np.array(test3)
        for i, n in enumerate(test1):
            if n < 4:
                test1_grade.append('F')
            if 4 <= n < 5:
                test1_grade.append('E')
            if 5 <= n < 6:
                test1_grade.append('D')
            if 6 <= n < 7:
                test1_grade.append('C')
            if 7 <= n < 8:
                test1_grade.append('B')
            if 8 <= n < 9:
                test1_grade.append('A')
            if 9 <= n <= 10:
                test1_grade.append('S')

        for i, n in enumerate(test2):
            if n < 4:
                test2_grade.append('F')
            if 4 <= n < 5:
                test2_grade.append('E')
            if 5 <= n < 6:
                test2_grade.append('D')
            if 6 <= n < 7:
                test2_grade.append('C')
            if 7 <= n < 8:
                test2_grade.append('B')
            if 8 <= n < 9:
                test2_grade.append('A')
            if 9 <= n < 11:
                test2_grade.append('S')
        for i, n in enumerate(test3):
            if n < 4:
                test3_grade.append('F')
            if 4 <= n < 5:
                test3_grade.append('E')
            if 5 <= n < 6:
                test3_grade.append('D')
            if 6 <= n < 7:
                test3_grade.append('C')
            if 7 <= n < 8:
                test3_grade.append('B')
            if 8 <= n < 9:
                test3_grade.append('A')
            if 9 <= n <= 10:
                test3_grade.append('S')
        return test1_grade, test2_grade, test3_grade


def find_grade_fromMark_predicted(predicted):
    predicted = np.array(predicted)
    retpred = []
    for i, n in enumerate(predicted):
        if n == 0:
            retpred.append('F')
        elif n == 1:
            retpred.append('E')
        elif n == 2:
            retpred.append('D')
        elif n == 3:
            retpred.append('C')
        elif n == 4:
            retpred.append('B')
        elif n == 5:
            retpred.append('A')
        elif n == 6:
            retpred.append('S')
    return retpred


def find_frequency_grades(test1, test2=None, test3=None):
    t1_fg_a = 0
    t1_fg_b = 0
    t1_fg_c = 0
    t1_fg_d = 0
    t1_fg_e = 0
    t1_fg_f = 0
    t1_fg_s = 0

    t2_fg_a = 0
    t2_fg_b = 0
    t2_fg_c = 0
    t2_fg_d = 0
    t2_fg_f = 0
    t2_fg_e = 0
    t2_fg_s = 0

    t3_fg_a = 0
    t3_fg_b = 0
    t3_fg_c = 0
    t3_fg_d = 0
    t3_fg_e = 0
    t3_fg_f = 0
    t3_fg_s = 0
    if test2 is None:

        for i in test1:
            if i == 'E':
                t1_fg_e = t1_fg_e + 1
            elif i == 'F':
                t1_fg_f = t1_fg_f + 1
            elif i == 'A':
                t1_fg_a = t1_fg_a + 1
            elif i == 'B':
                t1_fg_b = t1_fg_b + 1
            elif i == 'C':
                t1_fg_c = t1_fg_c + 1
            elif i == 'D':
                t1_fg_d = t1_fg_d + 1
            elif i == 'S':
                t1_fg_s = t1_fg_s + 1
        return t1_fg_a, t1_fg_b, t1_fg_c, t1_fg_d, t1_fg_e, t1_fg_f, t1_fg_s

    elif test3 is None:
        for i in test1:
            if i == 'E':
                t1_fg_e = t1_fg_e + 1
            elif i == 'F':
                t1_fg_f = t1_fg_f + 1
            elif i == 'A':
                t1_fg_a = t1_fg_a + 1
            elif i == 'B':
                t1_fg_b = t1_fg_b + 1
            elif i == 'C':
                t1_fg_c = t1_fg_c + 1
            elif i == 'D':
                t1_fg_d = t1_fg_d + 1
            elif i == 'S':
                t1_fg_s = t1_fg_s + 1

        for i in test2:
            if i == 'E':
                t2_fg_e = t2_fg_e + 1
            elif i == 'F':
                t2_fg_f = t2_fg_f + 1
            elif i == 'A':
                t2_fg_a = t2_fg_a + 1
            elif i == 'B':
                t2_fg_b = t2_fg_b + 1
            elif i == 'C':
                t2_fg_c = t2_fg_c + 1
            elif i == 'D':
                t2_fg_d = t2_fg_d + 1
            elif i == 'S':
                t2_fg_s = t2_fg_s + 1

        return t1_fg_a, t1_fg_b, t1_fg_c, t1_fg_d, t1_fg_e, t1_fg_f, t1_fg_s, \
               t2_fg_a, t2_fg_b, t2_fg_c, t2_fg_d, t2_fg_e, t2_fg_f, t2_fg_s
    else:
        for i in test1:
            if i == 'E':
                t1_fg_e = t1_fg_e + 1
            elif i == 'F':
                t1_fg_f = t1_fg_f + 1
            elif i == 'A':
                t1_fg_a = t1_fg_a + 1
            elif i == 'B':
                t1_fg_b = t1_fg_b + 1
            elif i == 'C':
                t1_fg_c = t1_fg_c + 1
            elif i == 'D':
                t1_fg_d = t1_fg_d + 1
            elif i == 'S':
                t1_fg_s = t1_fg_s + 1

        for i in test2:
            if i == 'E':
                t2_fg_e = t2_fg_e + 1
            elif i == 'F':
                t2_fg_f = t2_fg_f + 1
            elif i == 'A':
                t2_fg_a = t2_fg_a + 1
            elif i == 'B':
                t2_fg_b = t2_fg_b + 1
            elif i == 'C':
                t2_fg_c = t2_fg_c + 1
            elif i == 'D':
                t2_fg_d = t2_fg_d + 1
            elif i == 'S':
                t2_fg_s = t2_fg_s + 1
        for i in test3:
            if i == 'E':
                t3_fg_e = t3_fg_e + 1
            elif i == 'F':
                t3_fg_f = t3_fg_f + 1
            elif i == 'A':
                t3_fg_a = t3_fg_a + 1
            elif i == 'B':
                t3_fg_b = t3_fg_b + 1
            elif i == 'C':
                t3_fg_c = t3_fg_c + 1
            elif i == 'D':
                t3_fg_d = t3_fg_d + 1
            elif i == 'S':
                t3_fg_s = t3_fg_s + 1
        return t1_fg_a, t1_fg_b, t1_fg_c, t1_fg_d, t1_fg_e, t1_fg_f, t1_fg_s, \
               t2_fg_a, t2_fg_b, t2_fg_c, t2_fg_d, t2_fg_e, t2_fg_f, t2_fg_s, \
               t3_fg_a, t3_fg_b, t3_fg_c, t3_fg_d, t3_fg_e, t3_fg_f, t3_fg_s
















        # def create_teacher(num):
        #     for i in range(3, num):
        #         us = User.objects.create_user(username='teacher' + str(i),
        #                                       email='teacher' + str(i) + '@gmail.com',
        #                                       password='dnpandey')
        #         us.save()
        #         gr = Group.objects.get(name='Teachers')
        #         gr.user_set.add(us)
        #
        #         teach = Teacher(teacheruser=us, experience=5, name=us.username)
        #         teach.save()
        #
        #
        # def create_student(num):
        #     for i in range(4, num):
        #         us = User.objects.create_user(username='student' + str(i),
        #                                       email='studentss' + str(i) + '@gmail.com',
        #                                       password='dnpandey')
        #         us.save()
        #         gr = Group.objects.get(name='Students')
        #         gr.user_set.add(us)
        #         cl = klass.objects.all()
        #         classes = []
        #         for k in cl:
        #             classes.append(k)
        #         stu = Student(studentuser=us, klass=classes[0], rollNumber=int(str(i) + '00'), name='stu' + str(i),
        #                       dob=timezone.now(), pincode=int(str(405060)))
        #         stu.save()
        #         sub = Subject(name='Science', student=stu)
        #         sub.save()

    # def readmarks(user):
    #    profile = user.student
    #    subjects = user.student.subject_set.all()
    #    mathst1, mathst2, mathst3, mathshy, \
    #    mathst4, mathspredhy = [], [], [], [], [], []
    #    hindit1, hindit2, hindit3, hindihy, hindit4, \
    #    hindipredhy = [], [], [], [], [], []
    #    englisht1, englisht2, englisht3, englishhy, \
    #    englisht4, englishpredhy = [], [], [], [], [], []
    #    sciencet1, sciencet2, sciencet3, sciencehy, \
    #    sciencet4, sciencepredhy = [], [], [], [], [], []
    #
    #    for i in subjects:
    #        if i.name == 'Maths':
    #            mathst1.append(i.test1)
    #            mathst2.append(i.test2)
    #            mathst3.append(i.test3)
    #            mathshy.append(i.hy)
    #            mathst4.append(i.test4)
    #            mathspredhy.append(i.predicted_hy)
    #        elif i.name == 'Hindi':
    #            hindit1.append(i.test1)
    #            hindit2.append(i.test2)
    #            hindit3.append(i.test3)
    #            hindihy.append(i.hy)
    #            hindit4.append(i.test4)
    #            hindipredhy.append(i.predicted_hy)
    #        elif i.name == 'English':
    #            englisht1.append(i.test1)
    #            englisht2.append(i.test2)
    #            englisht3.append(i.test3)
    #            englishhy.append(i.hy)
    #            englisht4.append(i.test4)
    #            englishpredhy.append(i.predicted_hy)
    #        elif i.name == 'Science':
    #            sciencet1.append(i.test1)
    #            sciencet2.append(i.test2)
    #            sciencet3.append(i.test3)
    #            sciencehy.append(i.hy)
    #            sciencet4.append(i.test4)
    #
    #            sciencepredhy.append(i.predicted_hy)

    return mathst1, mathst2, mathst3, mathshy, mathst4, mathspredhy, \
           hindit1, hindit2, hindit3, hindihy, hindit4, hindipredhy, \
           englisht1, englisht2, englisht3, englishhy, englisht4, englishpredhy, \
           sciencet1, sciencet2, sciencet3, sciencehy, sciencet4, sciencepredhy


# class way

class Studs:
    def __init__(self, user):
        self.profile = user.student

    def my_subjects_objects(self):
        subs = self.profile.subject_set.all()
        subjects = []
        for sub in subs:
            subjects.append(sub)
        return subjects

    def my_subjects_names(self):
        subs = self.profile.subject_set.all()
        subjects = []
        for sub in subs:
            subjects.append(sub.name)
        subjects = list(unique_everseen(subjects))
        return subjects

    def readmarks(self):
        subjects = self.profile.subject_set.all()
        mathst1, mathst2, mathst3, mathshy, \
        mathst4, mathspredhy = [], [], [], [], [], []
        hindit1, hindit2, hindit3, hindihy, hindit4, \
        hindipredhy = [], [], [], [], [], []
        englisht1, englisht2, englisht3, englishhy, \
        englisht4, englishpredhy = [], [], [], [], [], []
        sciencet1, sciencet2, sciencet3, sciencehy, \
        sciencet4, sciencepredhy = [], [], [], [], [], []

        for i in subjects:
            if i.name == 'Maths':
                mathst1.append(i.test1)
                print(i.test1)
                mathst2.append(i.test2)
                mathst3.append(i.test3)
                mathshy.append(i.hy)
                mathst4.append(i.test4)
                mathspredhy.append(i.predicted_hy)
            elif i.name == 'Hindi':
                hindit1.append(i.test1)
                hindit2.append(i.test2)
                hindit3.append(i.test3)
                hindihy.append(i.hy)
                hindit4.append(i.test4)
                hindipredhy.append(i.predicted_hy)
            elif i.name == 'English':
                englisht1.append(i.test1)
                englisht2.append(i.test2)
                englisht3.append(i.test3)
                englishhy.append(i.hy)
                englisht4.append(i.test4)
                englishpredhy.append(i.predicted_hy)
            elif i.name == 'Science':
                sciencet1.append(i.test1)
                sciencet2.append(i.test2)
                sciencet3.append(i.test3)
                sciencehy.append(i.hy)
                sciencet4.append(i.test4)
            return mathst1, mathst2, mathst3, mathshy, mathst4, mathspredhy, \
                   hindit1, hindit2, hindit3, hindihy, hindit4, hindipredhy, \
                   englisht1, englisht2, englisht3, englishhy, englisht4, englishpredhy, \
                   sciencet1, sciencet2, sciencet3, sciencehy, sciencet4, sciencepredhy

    def predictionConvertion(self, prediction):
        try:
            prediction = prediction[0]
        except:
            pass

        if prediction == 0:
            conversion = 35
        elif prediction == 1:
            conversion = 45
        elif prediction == 2:
            conversion = 55
        elif prediction == 3:
            conversion = 65
        elif prediction == 4:
            conversion = 75
        elif prediction == 5:
            conversion = 85
        elif prediction == 6:
            conversion = 95
        else:
            conversion = '404'
        return conversion

    def allOnlinetests(self):
        my_tests = KlassTest.objects.filter(testTakers=self.profile)
        return my_tests

    def OnlineTestsSubwise(self, subject):
        my_tests = KlassTest.objects.filter(testTakers=self.profile, sub=
        subject)
        return my_tests

    def is_onlineTestTaken(self, test_id):
        try:
            test = OnlineMarks.objects.get(test__id=test_id, student=
            self.profile)
            return test
        except:
            return None

    def online_findAverageofTest(self, test_id, percent=None):
        if percent:
            test = OnlineMarks.objects.filter(test__id=test_id)
            all_marks = []
            all_marks_percent = []
            for te in test:
                all_marks.append(int(te.marks))
                all_marks_percent.append((te.marks / te.test.max_marks) * 100)
            average = np.mean(all_marks)
            percent_average = np.mean(all_marks_percent)
            return average, percent_average


        else:
            test = OnlineMarks.objects.filter(test__id=test_id)
            all_marks = []
            for te in test:
                all_marks.append(int(te.marks))
            average = np.mean(all_marks)

            return average

    def online_findPercentile(self, test_id):
        test = OnlineMarks.objects.filter(test__id=test_id)
        all_marks = []
        for te in test:
            all_marks.append(te.marks)
        num_students = len(all_marks)
        my_score = OnlineMarks.objects.get(test__id=test_id, student=
        self.profile)
        my_score = my_score.marks
        same_marks = -1
        less_marks = 0
        for i in all_marks:
            if i == my_score:
                same_marks += 1
            elif i < my_score:
                less_marks += 1
        percentile = ((less_marks + (0.5 * same_marks) * 100) / num_students)
        return percentile, all_marks

    def online_QuestionPercentage(self, test_id):
        online_marks = OnlineMarks.objects.filter(test__id=test_id)
        all_answers = []
        for aa in online_marks:
            all_answers.extend(aa.allAnswers)
        unique, counts = np.unique(all_answers, return_counts=True)
        freq = np.asarray((unique, counts)).T
        return freq


class Teach:
    def __init__(self, user):
        self.profile = user.teacher

    def my_classes_objects(self, klass_name=None):
        if klass_name:
            subs = self.profile.subject_set.all()
            if subs:
                klasses = []
                for sub in subs:
                    if sub.student.klass.name == klass_name:
                        klasses.append(sub.student.klass)
                return klasses[0]
            else:
                return None

        subs = self.profile.subject_set.all()
        if subs:
            klasses = []
            for sub in subs:
                klasses.append(sub.student.klass)
            return klasses
        else:
            return None

    def my_classes_names(self):
        subs = self.profile.subject_set.all()
        if subs:
            klasses = []
            for sub in subs:
                klasses.append(sub.student.klass.name)
            klasses = list(unique_everseen(klasses))
            return klasses
        else:
            return None

    def my_subjects_names(self):
        subs = self.profile.subject_set.all()
        subjects = []
        for i in subs:
            subjects.append(i.name)
        subjects = list(unique_everseen(subjects))
        return subjects

    def my_school(self):
        school = self.profile.school
        return school

    def listofStudents(self, klass):
        listofstudents = []
        subject_list = self.profile.subject_set.filter(student__klass__name=klass)
        for i in subject_list:
            listofstudents.append(i.student)
        return listofstudents

    def listofStudentsMarks(self, which_class):
        marks_class_test1 = []
        marks_class_test2 = []
        marks_class_test3 = []
        marks_class_predictedHy = []
        sub_class = self.profile.subject_set.filter(student__klass__name=which_class)
        print(sub_class)
        if not sub_class:
            pass
        else:
            for i in sub_class:
                if i.test1:
                    marks_class_test1.append(i.test1)
                if i.test2:
                    marks_class_test2.append(i.test2)
                if i.test3:
                    marks_class_test3.append(i.test3)
                if i.predicted_hy:
                    marks_class_predictedHy.append(i.predicted_hy)
        return marks_class_test1, marks_class_test2, marks_class_test3, marks_class_predictedHy

    def teacher_get_testmarks_classwise(req, klass_dict):
        klass_test1_dict = {}  # dictionary to hold test1 marks of different classes
        klass_test2_dict = {}
        klass_test3_dict = {}

        # fill out the above dictionaries

        for i in klass_dict.values():
            kk = i
            klasstest1 = []
            klasstest2 = []
            klasstest3 = []

            for j in kk:
                klasstest1.append(j.test1)
                klasstest2.append(j.test2)
                klasstest3.append(j.test3)
                testm1 = {str(j.student.klass): klasstest1}
                testm2 = {str(j.student.klass): klasstest2}
                testm3 = {str(j.student.klass): klasstest3}
            klass_test1_dict.update(testm1)
            klass_test2_dict.update(testm2)
            klass_test3_dict.update(testm3)
        return klass_test1_dict, klass_test2_dict, klass_test2_dict

    def find_frequency_grades(self, test1, test2=None, test3=None):
        t1_fg_a = 0
        t1_fg_b = 0
        t1_fg_c = 0
        t1_fg_d = 0
        t1_fg_e = 0
        t1_fg_f = 0
        t1_fg_s = 0

        t2_fg_a = 0
        t2_fg_b = 0
        t2_fg_c = 0
        t2_fg_d = 0
        t2_fg_f = 0
        t2_fg_e = 0
        t2_fg_s = 0

        t3_fg_a = 0
        t3_fg_b = 0
        t3_fg_c = 0
        t3_fg_d = 0
        t3_fg_e = 0
        t3_fg_f = 0
        t3_fg_s = 0
        if test2 is None:

            for i in test1:
                if i == 'E':
                    t1_fg_e = t1_fg_e + 1
                elif i == 'F':
                    t1_fg_f = t1_fg_f + 1
                elif i == 'A':
                    t1_fg_a = t1_fg_a + 1
                elif i == 'B':
                    t1_fg_b = t1_fg_b + 1
                elif i == 'C':
                    t1_fg_c = t1_fg_c + 1
                elif i == 'D':
                    t1_fg_d = t1_fg_d + 1
                elif i == 'S':
                    t1_fg_s = t1_fg_s + 1
            return t1_fg_a, t1_fg_b, t1_fg_c, t1_fg_d, t1_fg_e, t1_fg_f, t1_fg_s

        elif test3 is None:
            for i in test1:
                if i == 'E':
                    t1_fg_e = t1_fg_e + 1
                elif i == 'F':
                    t1_fg_f = t1_fg_f + 1
                elif i == 'A':
                    t1_fg_a = t1_fg_a + 1
                elif i == 'B':
                    t1_fg_b = t1_fg_b + 1
                elif i == 'C':
                    t1_fg_c = t1_fg_c + 1
                elif i == 'D':
                    t1_fg_d = t1_fg_d + 1
                elif i == 'S':
                    t1_fg_s = t1_fg_s + 1

            for i in test2:
                if i == 'E':
                    t2_fg_e = t2_fg_e + 1
                elif i == 'F':
                    t2_fg_f = t2_fg_f + 1
                elif i == 'A':
                    t2_fg_a = t2_fg_a + 1
                elif i == 'B':
                    t2_fg_b = t2_fg_b + 1
                elif i == 'C':
                    t2_fg_c = t2_fg_c + 1
                elif i == 'D':
                    t2_fg_d = t2_fg_d + 1
                elif i == 'S':
                    t2_fg_s = t2_fg_s + 1

            return t1_fg_a, t1_fg_b, t1_fg_c, t1_fg_d, t1_fg_e, t1_fg_f, t1_fg_s, \
                   t2_fg_a, t2_fg_b, t2_fg_c, t2_fg_d, t2_fg_e, t2_fg_f, t2_fg_s
        else:
            for i in test1:
                if i == 'E':
                    t1_fg_e = t1_fg_e + 1
                elif i == 'F':
                    t1_fg_f = t1_fg_f + 1
                elif i == 'A':
                    t1_fg_a = t1_fg_a + 1
                elif i == 'B':
                    t1_fg_b = t1_fg_b + 1
                elif i == 'C':
                    t1_fg_c = t1_fg_c + 1
                elif i == 'D':
                    t1_fg_d = t1_fg_d + 1
                elif i == 'S':
                    t1_fg_s = t1_fg_s + 1

            for i in test2:
                if i == 'E':
                    t2_fg_e = t2_fg_e + 1
                elif i == 'F':
                    t2_fg_f = t2_fg_f + 1
                elif i == 'A':
                    t2_fg_a = t2_fg_a + 1
                elif i == 'B':
                    t2_fg_b = t2_fg_b + 1
                elif i == 'C':
                    t2_fg_c = t2_fg_c + 1
                elif i == 'D':
                    t2_fg_d = t2_fg_d + 1
                elif i == 'S':
                    t2_fg_s = t2_fg_s + 1
            for i in test3:
                if i == 'E':
                    t3_fg_e = t3_fg_e + 1
                elif i == 'F':
                    t3_fg_f = t3_fg_f + 1
                elif i == 'A':
                    t3_fg_a = t3_fg_a + 1
                elif i == 'B':
                    t3_fg_b = t3_fg_b + 1
                elif i == 'C':
                    t3_fg_c = t3_fg_c + 1
                elif i == 'D':
                    t3_fg_d = t3_fg_d + 1
                elif i == 'S':
                    t3_fg_s = t3_fg_s + 1
            return t1_fg_a, t1_fg_b, t1_fg_c, t1_fg_d, t1_fg_e, t1_fg_f, t1_fg_s, \
                   t2_fg_a, t2_fg_b, t2_fg_c, t2_fg_d, t2_fg_e, t2_fg_f, t2_fg_s, \
                   t3_fg_a, t3_fg_b, t3_fg_c, t3_fg_d, t3_fg_e, t3_fg_f, t3_fg_s

    def find_grade_from_marks(self, test1, test2=None, test3=None):
        test1_grade = []
        test2_grade = []
        test3_grade = []
        test1 = np.array(test1)
        if test2 is None:
            for i, n in enumerate(test1):
                if n < 4:
                    test1_grade.append('F')
                if 4 <= n < 5:
                    test1_grade.append('E')
                if 5 <= n < 6:
                    test1_grade.append('D')
                if 6 <= n < 7:
                    test1_grade.append('C')
                if 7 <= n < 8:
                    test1_grade.append('B')
                if 8 <= n < 9:
                    test1_grade.append('A')
                if 9 <= n <= 10:
                    test1_grade.append('S')
            return test1_grade
        elif test3 is None:

            test2 = np.array(test2)

            for i, n in enumerate(test1):
                if n < 4:
                    test1_grade.append('F')
                if 4 <= n < 5:
                    test1_grade.append('E')
                if 5 <= n < 6:
                    test1_grade.append('D')
                if 6 <= n < 7:
                    test1_grade.append('C')
                if 7 <= n < 8:
                    test1_grade.append('B')
                if 8 <= n < 9:
                    test1_grade.append('A')
                if 9 <= n <= 10:
                    test1_grade.append('S')

            for i, n in enumerate(test2):
                if n < 4:
                    test2_grade.append('F')
                if 4 <= n < 5:
                    test2_grade.append('E')
                if 5 <= n < 6:
                    test2_grade.append('D')
                if 6 <= n < 7:
                    test2_grade.append('C')
                if 7 <= n < 8:
                    test2_grade.append('B')
                if 8 <= n < 9:
                    test2_grade.append('A')
                if 9 <= n <= 10:
                    test2_grade.append('S')
            return test1_grade, test2_grade
        else:
            test2 = np.array(test2)
            test3 = np.array(test3)
            for i, n in enumerate(test1):
                if n < 4:
                    test1_grade.append('F')
                if 4 <= n < 5:
                    test1_grade.append('E')
                if 5 <= n < 6:
                    test1_grade.append('D')
                if 6 <= n < 7:
                    test1_grade.append('C')
                if 7 <= n < 8:
                    test1_grade.append('B')
                if 8 <= n < 9:
                    test1_grade.append('A')
                if 9 <= n <= 10: test1_grade.append('S')

            for i, n in enumerate(test2):
                if n < 4:
                    test2_grade.append('F')
                if 4 <= n < 5:
                    test2_grade.append('E')
                if 5 <= n < 6:
                    test2_grade.append('D')
                if 6 <= n < 7:
                    test2_grade.append('C')
                if 7 <= n < 8:
                    test2_grade.append('B')
                if 8 <= n < 9:
                    test2_grade.append('A')
                if 9 <= n < 11:
                    test2_grade.append('S')
            for i, n in enumerate(test3):
                if n < 4:
                    test3_grade.append('F')
                if 4 <= n < 5:
                    test3_grade.append('E')
                if 5 <= n < 6:
                    test3_grade.append('D')
                if 6 <= n < 7:
                    test3_grade.append('C')
                if 7 <= n < 8:
                    test3_grade.append('B')
                if 8 <= n < 9:
                    test3_grade.append('A')
                if 9 <= n <= 10:
                    test3_grade.append('S')
            return test1_grade, test2_grade, test3_grade

    def averageoftest(self, test, test2=None, test3=None):
        if test2 is None and test3 is None:
            testmarks = np.array(test)
            return np.mean(testmarks)
        elif test3 is None:
            testmarks = np.array(test)
            testmarks2 = np.array(test2)
            return np.mean(testmarks), np.mean(testmarks2)
        else:
            testmarks = np.array(test)
            testmarks2 = np.array(test2)
            testmarks3 = np.array(test3)
            return np.mean(testmarks), np.mean(testmarks2), np.mean(testmarks3)

    def school_test_analysis(self, test):
        average_test = self.averageoftest(test)
        g1 = self.find_grade_from_marks(test)
        t1_fg_a, t1_fg_b, t1_fg_c, t1_fg_d, t1_fg_e, t1_fg_f, t1_fg_s = \
            self.find_frequency_grades(g1)
        context = \
            {'testav': average_test, 't1_fg_a': t1_fg_a, 't1_fg_b': t1_fg_b,
             't1_fg_c': t1_fg_c, 't1_fg_d': t1_fg_d, 't1_fg_e': t1_fg_e, 't1_fg_f': t1_fg_f,
             't1_fg_s': t1_fg_s}
        return context
    def online_findAverageofTest(self, test_id, percent=None):
        if percent:
            test = OnlineMarks.objects.filter(test__id=test_id)
            all_marks = []
            all_marks_percent = []
            for te in test:
                all_marks.append(int(te.marks))
                all_marks_percent.append((te.marks / te.test.max_marks) * 100)
            average = np.mean(all_marks)
            percent_average = np.mean(all_marks_percent)
            return average, percent_average


        else:
            test = OnlineMarks.objects.filter(test__id=test_id)
            all_marks = []
            for te in test:
                all_marks.append(int(te.marks))
            average = np.mean(all_marks)

            return average
    def online_freqeucyGrades(self,test_id):
        test = OnlineMarks.objects.filter(test__id = test_id)
        all_marks = []
        for i in test:
            all_marks.append((i.marks/i.test.max_marks)*100)
        grade_s = 0
        grade_a = 0
        grade_b = 0
        grade_c = 0
        grade_d = 0
        grade_e = 0
        grade_f = 0
        for marks in all_marks:
            if math.ceil(marks) < 33:
                grade_f +=1
            elif 33 <= math.ceil(marks) < 50:
                grade_e +=1
            elif 50 <= math.ceil(marks) < 60:
                grade_d +=1
            elif 60 <= math.ceil(marks) < 70:
                grade_c +=1
            elif 70 <= math.ceil(marks) < 80:
                grade_b +=1
            elif 80 <= math.ceil(marks) < 90:
                grade_a +=1
            elif 90 <= math.ceil(marks) <= 100:
                grade_s +=1
        return grade_s,grade_a,grade_b,grade_c,grade_d,grade_e,grade_f 

    def online_QuestionPercentage(self, test_id):
        online_marks = OnlineMarks.objects.filter(test__id=test_id)
        all_answers = []
        for aa in online_marks:
            all_answers.extend(aa.allAnswers)
        unique, counts = np.unique(all_answers, return_counts=True)
        freq = np.asarray((unique, counts)).T
        return freq
    def online_skippedQuestions(self,test_id):
        online_marks = OnlineMarks.objects.filter(test__id = test_id)
        skipped_questions = []
        for om in online_marks:
            for sq in om.skippedAnswers:
                skipped_questions.append(sq)
        unique, counts = np.unique(skipped_questions, return_counts=True)
        sq = np.asarray((unique, counts)).T
        return sq
        









