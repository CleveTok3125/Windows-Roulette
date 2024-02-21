import os, random
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_whitespace(string):
    result = ''
    for i, char in enumerate(string):
        if i > 0 and i % 3 == 0:
            result += ' '
        result += char
    return result

def remove_whitespace(string):
    return int(string.replace(' ', ''))

def for_input(ask, data_type=str):
    while True:
        try:
            ans = input(ask)
            if data_type == int:
                ans = int(ans)
            else:
                ans = str(ans)
            break
        except:
            pass
    return ans

def is_valid_player_num(player_num):
    try:
        if player_num > 0 and player_num <= 36:
            return True
        else:
            print('Số người chơi phải lớn hơn 0 và không lớn hơn 36.')
            return False
    except:
        return False

def is_valid_player_turn(player_turn, player_num):
    try:
        player_turn = int(player_turn)
        if player_turn > 0 and player_turn <= player_num:
            return True
        else:
            print('STT phải lớn hơn 0 và nhỏ hơn số người chơi.')
            return False
    except:
        return False

def is_valid_bullet_num(bullet_num):
    try:
        bullet_num = int(bullet_num)
        if bullet_num > 0 and bullet_num < 36:
            return True
        else:
            print('Số "đạn" phải lớn hơn 0 và nhỏ hơn 36')
            return False
    except:
        return False

def board_format(random_numbers):
    lists_of_numbers = [random_numbers[i:i+6] for i in range(0, 36, 6)]
    lists_of_strings = [' '.join(map(str, sublist)) for sublist in lists_of_numbers]
    board = '\n'.join(lists_of_strings)
    return board

def board_gen(raw_board, k):
    bullet = random.sample(raw_board, k)
    return bullet, raw_board

def refresh_board(raw_board, n):
    raw_board.remove(n)
    random.shuffle(raw_board)
    return raw_board

def is_valid_choice(raw_board, n):
    strnum = len(str(n))
    if n in raw_board and strnum == 3:
        return True
    elif strnum < 3:
        return True
    else:
        return False

def loser():
    #os.system("shutdown /s /t 30")
    for sec in range(30, 0, -1):
        print(f'Bạn đã bị loại. {sec}s đếm ngược...', end='\r')
        sleep(1)
    os._exit(0)

def winner():
    print('Trò chơi kết thúc!!!')
    for _ in range(30):
        sleep(1)
    os._exit(0)

if __name__ == '__main__':
    rule = '''Luật cơ bản của trò chơi:
Mỗi người chơi sẽ theo số thứ tự lần lượt "nổ súng". Nếu có người chơi xấu số trúng "đạn" sẽ bị loại khỏi trò chơi ngay lập tức, những người còn lại sẽ tiếp tục chơi cho đến khi chỉ còn lại một người. Người duy nhất còn sống sót sẽ là người chiến thắng!
Hướng dẫn cách chơi:
- Mỗi người chơi sẽ chạy chương trình này trên máy tính của mình, bảo đảm có thể giao tiếp với người chơi khác. Nhập ID phòng và số người chơi trong phòng đó, sau đó chọn số thứ tự (STT).
- Khi bắt đầu trò chơi, không được cho người chơi khác xem màn hình của mình cho đến khi có thông báo về người chiến thắng hoặc bạn bị loại.
- Trong khi chơi, người chơi luân phiên nhau theo thứ tự chọn ra một số trong bảng 6x6 đã cho trước, sau đó thông báo cho các người chơi khác con số mà mình chọn. Tất cả người chơi sẽ cùng nhập số mà người thông báo chọn. Quá trình này lặp lại kể cả khi có người bị loại. Khi hết bảng hoặc có người bị loại do trúng "đạn", một bảng mới sẽ được tạo và chuyển qua vòng mới.
- Để dành lấy chiến thắng thực sự, người chơi cần phải hợp tác với nhau để không để xảy ra bất kỳ sai sót nào. Nếu có người chơi bị loại mà không phải do trúng "đạn", lượt chọn của người chơi đó sẽ bị bỏ qua và tất cả người chơi còn lại phải đoán đúng số để sang lượt kế tiếp hoặc tìm ra được tên sát thủ.
- Ngoài ra khi số lượng người chơi lớn hơn 6, sẽ có ngẫu nhiên một người là sát thủ. Thay vì nhập số trong bảng 6x6, người chơi có thể nhập số thứ tự của người chơi khác trước khi có người thông báo chọn số trong bảng 6x6 để tìm ra sát thủ. Nếu đoán đúng, người đoán là người chiến thắng và trò chơi kết thúc. Nếu đoán sai, người đoán sẽ bị loại ngay lập tức. Lưu ý chỉ có thể đoán được sát thủ khi số người chơi còn sống lớn hơn 6, vi phạm coi như xử thua. Sát thủ sẽ có một đặc quyền là không bị loại khỏi trò chơi dù có bị trúng "đạn" mà vẫn sẽ được tham gia cùng những người chơi khác. Đặc quyền này chỉ hiệu lực duy nhất 1 lần.
Quy tắc phòng chơi:
- ID phòng là số nguyên tùy ý, có thể có dấu khoảng cách (space).
- Số lượng người chơi không quá 36 người.
- Không nhất thiết phải tạo phòng. Phòng được tạo ngay khi bắt đầu chơi. Đảm bảo các thông tin về ID phòng và số người chơi khớp nhau.
- STT phải là số nguyên dương, không lớn hơn số lượng người chơi, STT của các người chơi không trùng nhau. Không được có STT trống (không phải lượt của bất kỳ ai), nếu không sẽ tăng khả năng bị loại.
- Mỗi một vòng gồm tối đa 36 lượt, một màn chơi có thể gồm nhiều vòng. Số lượt càng tăng, tỷ lệ trúng "đạn" càng cao, bắt đầu từ 1/36, 1/35, 1/34,... cho đến 1/1.'''
    while True:
        print('''
            ,___________________________________________/7_
           |-_______------. `\                             |
       _,/ | _______)     |___\____________________________|
  .__/`((  | _______      | (/))_______________=.
     `~) \ | _______)     |   /----------------_/
       `__y|______________|  /
       / ________ __________/
      / /#####\(  \  /     ))
     / /#######|\  \(     //     __      __.__            .___                    
    / /########|.\_______//`    /  \    /  \__| ____    __| _/______  _  ________ 
   / /###(\)###||`------``      \   \/\/   /  |/    \  / __ |/  _ \ \/ \/ /  ___/ 
  / /##########||                \        /|  |   |  \/ /_/ (  <_> )     /\___ \  
 / /###########||                 \__/\  / |__|___|  /\____ |\____/ \/\_//____  > 
( (############||                      \/          \/      \/                 \/  
 \ \####(/)####))               __________             .__          __    __        
  \ \#########//                \______   \ ____  __ __|  |   _____/  |__/  |_  ____  
   \ \#######//                  |       _//  _ \|  |  \  | _/ __ \   __\   __\/ __ \ 
    `---|_|--`                   |    |   (  <_> )  |  /  |_\  ___/|  |  |  | \  ___/ 
       ((_))                     |____|_  /\____/|____/|____/\___  >__|  |__|  \___  >
        `-`                             \/                       \/                \/ 

1. Tạo phòng
2. Vào chơi
3. Tài liệu trò chơi (luật)
''')
        i1 = str(input('⁍ '))
        clear()
        if i1 == '1':
            print('Tạo phòng')
            ID = add_whitespace(str(random.randint(100000000, 999999999)))
            while True:
                player_num = for_input('Số người chơi: ', int)
                if is_valid_player_num(player_num):
                    break
            while True:
                bullet_num = for_input('Số "đạn" (đề xuất = 6): ', int)
                if is_valid_bullet_num(bullet_num):
                    break
            clear()
            print('ID phòng:', ID)
            print('Số người chơi:', player_num)
            input('\nGửi thông tin này tới các người chơi khác. <Enter để vào phòng> ')
            break
        elif i1 == '2':
            while True:
                try:
                    ID = for_input('Nhập ID phòng: ')
                    break
                except:
                    pass
            while True:
                player_num = for_input('Số người chơi: ', int)
                if is_valid_player_num(player_num):
                    break
            while True:
                bullet_num = for_input('Nhập số "đạn": ', int)
                if is_valid_bullet_num(bullet_num):
                    break
            break
        elif i1 == '3':
            print(rule)
            input('\n<Enter để tiếp tục>')
        else:
            os._exit(0)
        
        clear()
    clear()

print('Đợi người chơi khác để sẵn sàng...')
print('Nhấn Enter khi đã sẵn sàng.')
input()
print('Bắt đầu vào trò chơi.')

while True:
    player_turn = for_input('Chọn STT: ', int)
    if is_valid_player_turn(player_turn, player_num):
        break

ID = remove_whitespace(ID)
seed = int(str(ID)+str(player_num)+str(bullet_num))
random.seed(seed)

vip = False
if player_num > 6:
    imposter = random.randint(1, player_num)
    if player_turn == imposter:
        vip = True
        input('Bạn là sát thủ. Hãy cố gắng che dấu thân phận của mình. <Enter để tiếp tục> ')
else:
    imposter = float('-inf')

raw_board = random.sample(range(100, 1000), 36)
bullet, raw_board = board_gen(raw_board, bullet_num)

turn = 1
total_round = 1
rounds = 1
total_slot = 36
total_player = player_num
while True:
    clear()
    print('ID phòng:', ID)
    print('Số đạn:', bullet_num)
    print(f'Người chơi trúng đạn: {player_num-total_player}/{player_num}')
    print(f'Vòng {total_round} lượt {rounds}')
    print()

    if total_player == 0:
        input('Trò chơi đã kết thúc.')
        os._exit(0)
    if total_player == 1:
        print('Chúc mừng bạn là người thắng cuộc.')
        if player_turn == imposter:
            print('Sát thủ thắng.')
        winner()

    if turn == player_turn:
        is_player_turn = True
        board = board_format(raw_board)
        print(board)
        print('\nBạn có ' + str(round((1 - bullet_num/len(raw_board))*100, 2)) + '% cơ hội sống sót.')
        while True:
            num = for_input('Đã đến lượt của bạn. Chọn số trong bảng: ', int)
            if is_valid_choice(raw_board, num):
                break
            else:
                print('Vui lòng chọn số trong bảng')
    else:
        is_player_turn = False
        while True:
            num = for_input('Đợi người chơi khác thông báo và nhập số họ chọn hoặc đoán tên sát thủ: ', int)
            if len(str(num)) < 3 and is_player_turn == False and total_player <= 6:
                print('Số người còn lại quá ít để có thể chống lại tên sát thủ')
            else:
                break
        if not is_valid_choice(raw_board, num):
            print('Bạn đã không hợp tác với các người chơi khác.')
            total_player = 0
            loser()
    
    if len(str(num)) < 3 and is_player_turn == False:
        if num == imposter:
            print('Bạn là người tìm ra tên sát thủ. Tổ quốc ghi công bạn.')
            winner()
        else:
            print('Bạn đã đưa ra một lựa chọn sai lầm.')
            total_player = 0
            loser()
    elif len(str(num)) == 3:
        pass
    else:
        print('Mọi hành động nông nổi đều dẫn đến những hậu quả nghiêm trọng...')
        total_player = 0
        loser()

    if num == bullet and is_player_turn == True:
        total_slot = 0
        if vip == True:
            vip = False
            print('Shhh, hãy cố gắng đánh lạc hướng các người chơi khác để họ không biết bạn đã trúng "đạn".')
            sleep(1)
        else:
            print('Số phận đã chọn bạn.')
            total_player = 0
            loser()
    if num == bullet and is_player_turn == False:
        total_player -= 1
        total_slot = 0
        print('Đã có người chơi chọn phải ô có "đạn".')
        sleep(1)

    print('Chúc mừng bạn đã sống sót')
    sleep(1)

    if total_slot > 0:
        #raw_board = refresh_board(raw_board, num)
        total_slot -= 1
        rounds += 1

    if total_slot == 0:
        total_slot = 36
        total_round += 1
        rounds = 1

    raw_board = random.sample(range(100, 1000), total_slot)
    bullet, raw_board = board_gen(raw_board, bullet_num)

    if turn >= player_num:
        turn = 1
    else:
        turn += 1