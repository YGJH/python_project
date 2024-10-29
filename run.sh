set -e

for ((i = 1 ; i <= 100 ; i++))
do
    echo $i > input
    echo python3 ac.py < input > ac.out
    echo python3 wa.py < input > wa.out
    diff ac.out wa.out || break
done