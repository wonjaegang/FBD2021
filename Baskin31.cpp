#include <iostream>
#include <stdlib.h>

using namespace std;

void shuffle(int* arr, int num)
{
    int temp;
    int rn;
    for (int i = 0; i < num - 1; i++) {
        rn = rand() % (num - i) + i; // i 부터 num-1 사이에 임의의 정수 생성  (순서 정하기)
        temp = arr[i];
        arr[i] = arr[rn];
        arr[rn] = temp;
    }
}

bool check(int num)
{
    //31 체크하기
    if (num == 31) {
        return true;
    } else
        return false;
}

int game()
{
    int num = 1;
    int count = 0; // 숫자 몇개 말했는지 count
    int turns[3] = { 0, 1, 2 }; // 순서 배열 0: 경호 1: 경민 2: 재원
    shuffle(turns, 3); // 순서 정하기
    int turn_index = 0; // 순서 배열 index

    while (true) {
        if (turns[turn_index] == 0) {
            count = 0;
            // cout << "kyungho: ";
            for (int i = 0; i < rand() % 3 + 1; i++) {
                // cout << num << " ";
                count++;
                if (num == 28 || num == 29 || num == 22 || num == 15 || num == 8) {
                    if (count != 3) {
                        num++;
                        i++;
                        // cout << num << " ";
                    }
                }
                if (num == 10 || num == 18 || num == 25 || num == 30) {
                    num++;
                    break;
                }
                if (check(num)) {
                    return turns[turn_index];
                }
                num++;
            }
            // cout << endl;

            turn_index++;
            if (turn_index == 3) {
                turn_index = 0;
            }
        } else if (turns[turn_index] == 1) {
            // cout << "kyeongmin: ";
            int mod = num % 7;
            int end = 0;
            switch (mod) {
            case 0:
                if (num == 28)
                    end = num + (rand() % 2 + 1);
                else
                    end = num + 2;
                break;
            case 1:
                if (num == 29)
                    end = num + (rand() % 2);
                else
                    end = num + 1;
                break;
            case 2:
                end = num + 0;
                break;
            case 3:
                end = num + 0;
                break;
            case 4:
                end = num + 2;
                break;
            case 5:
                end = num + 2;
                break;
            case 6:
                end = num + 2;
                break;
            }
            num = end;
            // cout << num << " ";
            // cout << endl;
            if (check(num)) {
                return turns[turn_index];
            }
            num++;
            turn_index++;
            if (turn_index == 3) {
                turn_index = 0;
            }
        } else {
            // cout << "jaewon: ";
            for (int i = 0; i < rand() % 3 + 1; i++) {
                // cout << num << " ";
                if (num == 30) {
                    num++;
                    break;
                }
                if (check(num)) {
                    return turns[turn_index];
                }
                num++;
            }
            // cout << endl;

            turn_index++;
            if (turn_index == 3) {
                turn_index = 0;
            }
        }
    }
}

int main(int argc, char* argv[])
{
    srand((unsigned int)time(NULL));
    int lose[3] = { 0 }; // 패배수 저장
    int games = 100; // 게임수
    // int games = atoi(argv[1]);
    cout << "게임 수: " << games << " " << endl;
    for (int i = 0; i < games; i++) {
        int player = game();
        switch (player) {
        case 0:
            //cout << "경호 패배" << endl;
            lose[0]++;
            break;
        case 1:
            //cout << "경민 패배" << endl;
            lose[1]++;
            break;
        case 2:
            //cout << "재원 패배" << endl;
            lose[2]++;
            break;
        }
    }
    cout << "경호 승률: " << (games - lose[0]) / (double)games << "%" << endl;
    cout << "경민 승률: " << (games - lose[1]) / (double)games << "%" << endl;
    cout << "재원 승률: " << (games - lose[2]) / (double)games << "%" << endl;
}
