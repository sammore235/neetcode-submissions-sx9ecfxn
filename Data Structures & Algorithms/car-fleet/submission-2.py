class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [ (x,y) for x,y in zip(position,speed)]
        pair.sort(reverse=True)
        ds = []
        for p,s in pair:
            ds.append((target - p)/s)
            #print(ds)
            if len(ds)>=2 and ds[-1]<= ds[-2]:
                #print("Enter")
                ds.pop()
        return len(ds)
        ## What code I tried
        # milesleft =[]
        # hours =[]
        # ps = list(position)
        # print(ps)
        # for i in position:
        #     k = target -i
        #     #print(k)
        #     milesleft.append(k)
        # for j in range(0,len(milesleft)):
        #     ms = milesleft[j]/speed[j]
        #     #print(ms)
        #     hours.append(ms)
        # print(hours)
        # largest_hours = max(hours)
        # print(largest_hours)
        # for l in range(0,target):
        #     ps = [x + y for x, y in zip(ps, speed)]
        #     # After l hours
        #     print(ps)
        #     for m in ps:
        #         if m ==target:
        #             count =1
        #         else:
        #             continue
        #     # for m in range(1,target):
        #     #     continue
        #     #     #after 1 hr

        # no_of_carfleet = list(set(hours))
        # print(no_of_carfleet)
        # return len(no_of_carfleet)