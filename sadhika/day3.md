***25 - 07 - 26***



prblm:704:(binaty search):



if target is found return index value

if  target is not found return -1





coding:

class Solution:

&#x20;   def search(self, nums,target):

&#x20;       for i in range(len(nums)):

&#x20;           if nums\[i] == target:

&#x20;               return i

&#x20;       return -1



output=4



(optimal coding):



class Solution:

&#x20;   def search(self, nums,target):

&#x20;       left = 0

&#x20;       right = len(nums) -1

&#x20;       while left<=right:

&#x20;           mid =(left+right) //  2

&#x20;           if nums\[mid] == target:

&#x20;               return mid

&#x20;           elif nums\[mid]<target:

&#x20;               left = mid+1

&#x20;           else:

&#x20;               right = mid -1

&#x20;       return -1



output = 4



prblm:35:(search the insert position)



coding:

class Solution:

&#x20;   def searchInsert(self, nums: List\[int], target: int) -> int:

&#x20;       left = 0

&#x20;       right = len(nums) -1

&#x20;       while left<=right:

&#x20;           mid =(left+right) //  2

&#x20;           if nums\[mid] == target:

&#x20;               return mid

&#x20;           elif nums\[mid]<target:

&#x20;               left = mid+1

&#x20;           else:

&#x20;               right = mid -1

&#x20;       return left  



output=2



prblm:34



coding:



class Solution:

&#x20;   def searchRange(self, nums: List\[int], target: int) -> List\[int]:

&#x20;       first = -1

&#x20;       last = -1 

&#x20;       for i in range(len(nums)):

&#x20;           if nums\[i] == target:

&#x20;               if first == -1:

&#x20;                   first = i

&#x20;               last = i

&#x20;       return \[first,last]



output = \[3,4]



prblm:167 (two sum ||)



coding:

class Solution:

&#x20;   def twoSum(self, nums: List\[int], target: int) -> List\[int]:

&#x20;       for i in range(len(nums)):

&#x20;           for j in range(i+1 , len(nums)):

&#x20;               if nums\[i] + nums\[j] == target:

&#x20;                   return\[i+1,j+1]



class Solution:

&#x20;   def twoSum(self, nums: List\[int], target: int) -> List\[int]:

&#x20;      left = 0

&#x20;      right = len(nums) - 1

&#x20;      while left < right:

&#x20;       current\_sum = nums\[left] + nums\[right]

&#x20;       if current\_sum == target:

&#x20;           return \[left+1,right+1]

&#x20;       elif current\_sum < target:

&#x20;           left+=1

&#x20;       else:

&#x20;           right -=1

output=\[1,2]

prblm:11 (container with most water)





coding:

class Solution:

&#x20;   def maxArea(self, height: List\[int]) -> int:

&#x20;       maxA = 0

&#x20;       for i in range(len(height)):

&#x20;           for j in range(i+1,len(height)):

&#x20;               area = min(height\[i],height\[j])\*(j-i)

&#x20;               maxA = max(area,maxA)

&#x20;       return maxA



case 2:

class Solution:

&#x20;   def maxArea(self, height: List\[int]) -> int:

&#x20;       left = 0

&#x20;       right =len(height) -1

&#x20;       max\_area = 0

&#x20;       while left < right:

&#x20;           width = right - left

&#x20;           current\_height = min(height\[left],height\[right])

&#x20;           area = width \* current\_height

&#x20;           max\_area = max(max\_area,area)

&#x20;           if height\[left] < height\[right]:

&#x20;               left += 1

&#x20;           else:

&#x20;               right -= 1

&#x20;       return max\_area



output= 49



prblm:977



coding:

class Solution:

&#x20;   def sortedSquares(self, nums: List\[int]) -> List\[int]:

&#x20;       answer = \[]

&#x20;       for i in nums:

&#x20;           answer.append(i\*i)

&#x20;       answer.sort()

&#x20;       return answer



output=\[0,1,9,16,100]



***27 - 07 - 26***



prblm:392



coding:(brute)

class Solution:

&#x20;   def isSubsequence(self, s: str, t: str) -> bool:

&#x20;       start = 0

&#x20;       for i in s:

&#x20;           found = False

&#x20;           for j in range(start,len(t)):

&#x20;               if i == t\[j]:

&#x20;                   found = True

&#x20;                   start = j+1

&#x20;                   break

&#x20;           if not found:

&#x20;               return False

&#x20;       return True



coding:(optimal)



class Solution:

&#x20;   def isSubsequence(self, s: str, t: str) -> bool:

&#x20;       i,j=0,0

&#x20;       while i <len(s) and j<len(t):

&#x20;           if s\[i] == t\[j]:

&#x20;               i+=1

&#x20;           j+=1

&#x20;       return i == len(s) 



output=true



prblm:344

coding:(optimal)



class Solution:

&#x20;   def reverseString(self, s: List\[str]) -> None:

&#x20;       new = \[]

&#x20;       for i in range(len(s)-1,-1,-1):

&#x20;           new.append(s\[i])

&#x20;       for i in range(len(new)):

&#x20;           s\[i] = new\[i]

&#x20;       return len(new)





coding:brute



class Solution:

&#x20;   def reverseString(self, s: List\[str]) -> None:

&#x20;      s.reverse()



output=\["o","l","L","e","h"]



prblm:

coding:(optimal)



class Solution:

&#x20;   def reverseWords(self, s: str) -> str:

&#x20;       word = s.split()

&#x20;       word.reverse()

&#x20;       return " ".join(word)



prblm:125



coding:

class Solution:

&#x20;   def isPalindrome(self, s: str) -> bool:

&#x20;       clean =""

&#x20;       for i in s:

&#x20;           if i.isalnum():

&#x20;               clean+=i.lower()

&#x20;       return clean ==clean\[::-1]





prblm:415(add string)



ascii code of A = 64

&#x20;             a = 97

&#x20;             0 = 48(started value)



coding:

class Solution:

&#x20;   def addStrings(self, num1: str, num2: str) -> str:

&#x20;       i = len(num1) - 1

&#x20;       j = len(num2) - 1

&#x20;       carry = 0

&#x20;       result = \[]

&#x20;       while i >= 0 or j >= 0 or carry:

&#x20;           digit1=0

&#x20;           digit2=0

&#x20;           if i>=0:

&#x20;               digit1 = ord(num1\[i]) - ord('0')

&#x20;               i =i-1

&#x20;           if j>=0:

&#x20;               digit2 = ord(num2\[j]) - ord('0')

&#x20;               j = j-1

&#x20;           total=digit1+digit2+carry

&#x20;           result.append(str(total % 10))

&#x20;           carry= total // 10

&#x20;       return "".join(result\[::-1])





***28 - 07 -26***



prblm:3



coding:(brute)



class Solution:

&#x20;   def lengthOfLongestSubstring(self, s: str) -> int:

&#x20;       maximum=0

&#x20;       for i in range(len(s)):

&#x20;           seen=set()

&#x20;           for j in range(i,len(s)):

&#x20;               if s\[j] in seen:

&#x20;                   break

&#x20;               seen.add(s\[j])

&#x20;               maximum=max(maximum,j-i+1)

&#x20;       return maximum

&#x20;       



coding:(optimal):



lass Solution:

&#x20;   def lengthOfLongestSubstring(self, s: str) -> int:

&#x20;       seen=set()

&#x20;       left=0

&#x20;       maximum=0

&#x20;       for r in range(len(s)):

&#x20;           while s\[r] in seen:

&#x20;               seen.remove(s\[left])

&#x20;               left+=1

&#x20;           seen.add(s\[r])

&#x20;           maximum=max(maximum,r-left+1)

&#x20;       return maximum

&#x20;      

output=3



prblm:209(optimal):(minimum size subarray sum)



min=inf

max=-inf





coding:

class Solution:

&#x20;   def minSubArrayLen(self, target: int, nums: List\[int]) -> int:

&#x20;       left=0

&#x20;       current\_sum=0

&#x20;       minimum=float('inf')

&#x20;       for right in range(len(nums)):

&#x20;           current\_sum+=nums\[right]

&#x20;           while current\_sum>=target:

&#x20;               minimum=min(minimum,right-left+1)

&#x20;               current\_sum-=nums\[left]

&#x20;               left+=1

&#x20;       if minimum==float('inf'):

&#x20;           return 0

&#x20;       return minimum





prblm:643:(maximum average subarray)



coding:



class Solution:

&#x20;   def findMaxAverage(self, nums: List\[int], k: int) -> float:

&#x20;       window\_sum=sum(nums\[:k]) #sum of first k window

&#x20;       maximum\_window=window\_sum

&#x20;       #inside the window

&#x20;       for i in range(k,len(nums)):

&#x20;           window\_sum=window\_sum+nums\[i]

&#x20;           window\_sum=window\_sum-nums\[i-k]

&#x20;           maximum\_window=max(maximum\_window,window\_sum)

&#x20;       return maximum\_window/k



output=4





prblm:1004:

coding:



class Solution:

&#x20;   def longestOnes(self, nums: List\[int], k: int) -> int:

&#x20;       left=0

&#x20;       zero\_count=0

&#x20;       maximum=0

&#x20;       for right in range(len(nums)):

&#x20;           if nums\[right]==0:

&#x20;               zero\_count+=1

&#x20;           while zero\_count>k:

&#x20;               if nums\[left]==0:

&#x20;                   zero\_count-=1

&#x20;               left+=1

&#x20;           maximum=max(maximum,right-left+1)

&#x20;       return maximum



output=6



***29 - 07 - 26***



prblm: 1(two sum):



coring:(brute):



class Solution:

&#x20;   def twoSum(self, nums: List\[int], target: int) -> List\[int]:

&#x20;       for i in range(len(nums)):

&#x20;           for j in range(i+1,len(nums)):

&#x20;               if nums\[i] + nums \[j] == target:

&#x20;                   return \[i,j]

&#x20;       

coding:(optimal):



class Solution:

&#x20;   def twoSum(self, nums: List\[int], target: int) -> List\[int]:

&#x20;       d ={} #number->index

&#x20;       for i in range(len(nums)):

&#x20;           c = target-nums\[i]

&#x20;           if c in d:

&#x20;               return\[d\[c],i]

&#x20;           d\[nums\[i]]=i



output=\[0,1]



prblm:205



coding:(brute)



class Solution:

&#x20;   def isIsomorphic(self, s: str, t: str) -> bool:

&#x20;       mapST={}

&#x20;       mapTS={}

&#x20;       for i in range(len(s)):

&#x20;           ch1 = s\[i]

&#x20;           ch2 = t\[i]

&#x20;           if ch1 in mapST:

&#x20;               if mapST\[ch1]!=ch2:

&#x20;                   return False

&#x20;           else:

&#x20;               mapST\[ch1]=ch2

&#x20;           if ch2 in mapTS:

&#x20;               if mapTS\[ch2]!= ch1:

&#x20;                   return False

&#x20;           else:

&#x20;               mapTS\[ch2]=ch1

&#x20;       return True



output=true



prblm:242:(anagram):



coding:

class Solution:

&#x20;   def isAnagram(self, s: str, t: str) -> bool:

&#x20;       if len(s) != len(t):

&#x20;           return False

&#x20;       return sorted(s) == sorted(t)



output=true



prblm:128:



coding:(brute):



class Solution:

&#x20;   def longestConsecutive(self, nums: List\[int]) -> int:

&#x20;       longest=0

&#x20;       for i in nums:

&#x20;           length = 1

&#x20;           while i + 1 in nums:

&#x20;               i+=1

&#x20;               length+=1

&#x20;           longest=max(longest,length)

&#x20;       return longest



coding:(optimal):



class Solution:

&#x20;   def longestConsecutive(self, nums: List\[int]) -> int:

&#x20;      ns = set(nums)

&#x20;      longest=0

&#x20;      for i in ns:

&#x20;       if i-1 not in ns:

&#x20;           length=1

&#x20;           while i+1 in ns:

&#x20;               i+=1

&#x20;               length+=1

&#x20;           longest=max(length,longest)

&#x20;      return longest

&#x20;   output=4



***30 - 07 - 26***



linkrd - list  :



prblm:(83):



coding:

class Solution:

&#x20;   def deleteDuplicates(self, head: Optional\[ListNode]) -> Optional\[ListNode]:

&#x20;       current = head

&#x20;       while current and current.next:

&#x20;           if current.val==current.next.val:

&#x20;               current.next=current.next.next

&#x20;           else:

&#x20;               current=current.next

&#x20;       return head



output=\[1,2]





prblm:206:(reverse linked list):



coding:



lass Solution:

&#x20;   def reverseList(self, head: Optional\[ListNode]) -> Optional\[ListNode]:

&#x20;       prev = None

&#x20;       current = head

&#x20;       while current:

&#x20;           #save the next node

&#x20;           next\_node=current.next

&#x20;           #reverse the pointer

&#x20;           current.next=prev

&#x20;           prev=current

&#x20;           current=next\_node

&#x20;       return prev



output=\[5,4,3,2,1]

* ***31 - 07 - 26***
* 



prblm:237:(delete node in a LL):



coding:

class Solution:

&#x20;   def deleteNode(self, node):

&#x20;       """

&#x20;       :type node: ListNode

&#x20;       :rtype: void Do not return anything, modify node in-place instead.

&#x20;       """

&#x20;       node.val=node.next.val  #copy the data node

&#x20;       node.next=node.next.next  #skip the value 



prblm:19:(remove Nth node from end of list)



coding:



\# Definition for singly-linked list.

\# class ListNode:

\#     def \_\_init\_\_(self, val=0, next=None):

\#         self.val = val

\#         self.next = next

class Solution:

&#x20;   def removeNthFromEnd(self, head: Optional\[ListNode], n: int) -> Optional\[ListNode]:

&#x20;       length = 0

&#x20;       current=head

&#x20;       while current:

&#x20;           length+=1

&#x20;           current=current.next

&#x20;       if length == n:

&#x20;           return head.next

&#x20;       current=head

&#x20;       for i in range(length - n - 1):

&#x20;           current=current.next

&#x20;       current.next=current.next.next

&#x20;       return head



output=\[1,2,3,5]



prblm:23(merge the LL)



coding:



class Solution:

&#x20;   def mergeTwoLists(self, list1: Optional\[ListNode], list2: Optional\[ListNode]) -> Optional\[ListNode]:

&#x20;       dummy=ListNode(0)

&#x20;       current=dummy

&#x20;       while list1 and list2:

&#x20;           if list1.val<list2.val:

&#x20;               current.next=list1

&#x20;               list1=list1.next

&#x20;           else:

&#x20;               current.next=list2

&#x20;               list2=list2.next

&#x20;           current=current.next

&#x20;       if list1:

&#x20;           current.next=list1

&#x20;       else:

&#x20;           current.next=list2

&#x20;       return dummy.next



output=\[1,1,2,3,4,4]



prblm:82:(remove dup from sorted LL):



coding:

\# Definition for singly-linked list.

\# class ListNode:

\#     def \_\_init\_\_(self, val=0, next=None):

\#         self.val = val

\#         self.next = next

class Solution:

&#x20;   def deleteDuplicates(self, head: Optional\[ListNode]) -> Optional\[ListNode]:

&#x20;       dummy=ListNode(0)

&#x20;       dummy.next=head

&#x20;       current=dummy

&#x20;       while current.next and current.next.next:

&#x20;           if current.next.val==current.next.next.val:

&#x20;               dup=current.next.val

&#x20;               while current.next and current.next.val==dup:

&#x20;                   current.next=current.next.next

&#x20;           else:

&#x20;               current=current.next

&#x20;       return dummy.next

output=\[1,2,5]



prblm:876(middle of the LL):

coding:





\# Definition for singly-linked list.

\# class ListNode:

\#     def \_\_init\_\_(self, val=0, next=None):

\#         self.val = val

\#         self.next = next

class Solution:

&#x20;   def deleteDuplicates(self, head: Optional\[ListNode]) -> Optional\[ListNode]:

&#x20;       dummy=ListNode(0)

&#x20;       dummy.next=head

&#x20;       current=dummy

&#x20;       while current.next and current.next.next:

&#x20;           if current.next.val==current.next.next.val:

&#x20;               dup=current.next.val

&#x20;               while current.next and current.next.val==dup:

&#x20;                   current.next=current.next.next

&#x20;           else:

&#x20;               current=current.next

&#x20;       return dummy.next

output=true



prblm:141:(linked list cycle)



coding:

class Solution:

&#x20;   def hasCycle(self, head: Optional\[ListNode]) -> bool:

&#x20;       visited=set()

&#x20;       current=head

&#x20;       while current:

&#x20;           if current in visited:

&#x20;               return True

&#x20;           visited.add(current)

&#x20;           current=current.next

&#x20;       return False



prblm:234:(palindrome LL):

coding:



class Solution:

&#x20;   def isPalindrome(self, head: Optional\[ListNode]) -> bool:

&#x20;       new=\[]

&#x20;       while head:

&#x20;           new.append(head.val)

&#x20;           head=head.next

&#x20;       return new==new\[::-1]

output=true





***01 - 08 - 26*** 





prblm:143:(reorder List):



coding:

class Solution:

&#x20;   def reorderList(self, head: Optional\[ListNode]) -> None:

&#x20;       """

&#x20;       Do not return anything, modify head in-place instead.

&#x20;       """

&#x20;       if not head:

&#x20;           return

&#x20;       nodes=\[]

&#x20;       current=head

&#x20;       while current:

&#x20;           nodes.append(current)

&#x20;           current=current.next

&#x20;       left=0

&#x20;       right=len(nodes)-1

&#x20;       while left<right:

&#x20;           nodes\[left].next=nodes\[right]

&#x20;           left+=1

&#x20;           if left == right:

&#x20;               break

&#x20;           nodes\[right].next=nodes\[left]

&#x20;           right-=1

&#x20;       nodes\[left].next=None

&#x20;       

output=\[1,4,2,3]



prblm:92:(reverse LL ||):



coding:



\# Definition for singly-linked list.

\# class ListNode:

\#     def \_\_init\_\_(self, val=0, next=None):

\#         self.val = val

\#         self.next = next

class Solution:

&#x20;   def reverseBetween(self, head: Optional\[ListNode], left: int, right: int) -> Optional\[ListNode]:

&#x20;       if not head or left == right:

&#x20;           return head

&#x20;       dummy=ListNode(0)

&#x20;       dummy.next=head

&#x20;       prev=dummy

&#x20;       for i in range(left - 1):

&#x20;           prev=prev.next

&#x20;       current=prev.next

&#x20;       for i in range(right-left):

&#x20;           next\_node=current.next

&#x20;           current.next=next\_node.next

&#x20;           next\_node.next=prev.next

&#x20;           prev.next=next\_node

&#x20;       return dummy.next



output:\[1,4,3,2,5]





stack:



stack=\[]

def push():

&#x20;   if len(stack)>num:

&#x20;       print("stack overflow")

&#x20;   else:

&#x20;       element=int(input("enter a the element:"))

&#x20;       stack.append(element)

&#x20;       print("element pushed successfully...!")

def pop():

&#x20;   pop\_element.pop()

&#x20;   print("the popped element:",pop\_element)

def peek():

&#x20;   print("top most elements:",stack\[-1])

def empty():

&#x20;   if len(stack)==0:

&#x20;       print("stack is empty...!")

&#x20;   else:

&#x20;       print("stack is:",stack)

num=int(input("enter the size of stack:"))

while True:

&#x20;   print("1.push")

&#x20;   print("2.pop")

&#x20;   print("3.peek")

&#x20;   print("4.empty")

&#x20;   print("5.exit")

&#x20;   option=int(input("choose number from the above:"))

&#x20;   if option==1:

&#x20;       push()

&#x20;   elif option==2:

&#x20;       pop()

&#x20;   elif option==3:

&#x20;       peek()

&#x20;   elif option==4:

&#x20;       empty()

&#x20;   elif option==5:

&#x20;       break

&#x20;   else:

&#x20;       print("invalid")

&#x20;       





