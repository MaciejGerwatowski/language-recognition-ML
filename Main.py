import Methods
from Methods import load_file, train_language, check_language, full_trained_perceptron, clasification, \
    percentage_of_agreement, load_text
import Perceptron
import GUI
import Methods2
from Methods2 import classify2
from Perceptron2 import Perceptron2

correct_answers = ['Angielski', 'Niemiecki', 'Francuski', 'Angielski', 'Polski', 'Czeski', 'Francuski', 'Wloski', 'Polski', 'Niemiecki', 'Angielski', 'Czeski']
#
# print(percentage_of_agreement(correct_answers, clasification("Test")), '% poprawnie zakfalifikowanych')

gui = GUI.GUI()


#print(percentage_of_agreement(correct_answers, Methods2.clasification2("Test")))

