def red_and_blue():
    t = int(input())

    for _ in range(t):
        n = int(input())
        r = list(map(int, input().split()))
        m = int(input())
        b = list(map(int, input().split()))
        
        
        def get_max_sum(arr_list):
            max_sum = 0
            current = 0
            for num in arr_list:
                current += num
                if max_sum < current:
                    max_sum = current
            return max_sum
        
        print(get_max_sum(r) + get_max_sum(b))    
    
if __name__ == "__main__":
    red_and_blue()
    
