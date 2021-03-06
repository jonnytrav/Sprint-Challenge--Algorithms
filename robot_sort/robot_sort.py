class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort_check(self):
        while self.light_is_on() == False and self.can_move_right() == True:
            self.set_light_on()
            self.swap_item()
            self.move_right()
            if self.compare_item() == -1:
                # next two lines returns it to its original place
                self.move_left()
                self.swap_item()
                # next line return
                self.move_right()
                self.set_light_off()
            elif self.compare_item() == 1:
                return False
            elif self.can_move_right() == False:
                return True

    def sort(self):
        """
        Sort the robot's list.
        """
        while self.light_is_on() == False:
            # light on while sorting
            self.set_light_on()
            self.swap_item()

            while self.can_move_right() == True:
                # stops when end of list is reached

                if self.compare_item() == 1:
                    # if held item is larger:
                    # next two lines move held item forward and keep continue loop
                    # by setting light to off
                    self.move_right()
                    self.set_light_off()
                    # now ready to iterate again and see if it's still the larger value

                elif self.compare_item() == -1:
                    # if held item is smaller than the next, grab larger item and continue
                    self.swap_item()
                    self.move_right()
                    if self.can_move_right() == False:
                        self.set_light_off()
                        break
                    self.set_light_off()

                    # ready to iterate again as long as we can still move right
                    # once we can't move right, below loop runs to begin again at the beginning
                    # and bring next largest value to the right end of array

            while self.can_move_left() == True:
                self.move_left()


#  *********************** separating code *************************************************

        # reapproaching with while loops and no additional helper methods
        # not a very timely solution
        # while self.light_is_on() == False:
        #     # light on while sorting
        #     self.set_light_on()

        #     while self.can_move_right() == True:
        #         # stops when end of list is reached
        #         # robot starts off with self._item set to None
        #         # self.set_light_on()
        #         self.swap_item()
        #         self.move_right()

        #         if self.compare_item() == 1:
        #             # held item is larger
        #             # next three lines move the smaller value to the left
        #             self.swap_item()
        #             self.move_left()
        #             self.swap_item()
        #             # next two pick up the next item
        #             self.move_right()
        #             self.set_light_off()
        #             # now ready to pick up where we left off

        #         elif self.compare_item() == -1:
        #             # if this item is smaller than the next, move it back to the left
        #             self.move_left()
        #             self.swap_item()
        #             self.move_right()
        #             self.set_light_off()
        #             # ready to pick up where we left off again
        #             # as long as we can still move right
        #             # once we can't move right, below loop runs
        #     while self.can_move_left():
        #         self.move_left()
# *************************** separating different blocks of code ***********************************
        # self.set_light_on()
        # while self.light_is_on == True:
        #     # will turn off when sorted
        #     for i in range(len(self._list)):
        #         while self.can_move_right() == True:
        #             for j in self._list[i + 1:]:
        #                 if self.compare_item() == 1:
        #                     self.move_right()
        #                 elif self.compare_item() == -1:
        #                     self.swap_item()
        #                     self.move_right()
        #         while self.can_move_left() == True:
        #             self.move_left()
        #     if i == len(self._list) - 1:
        #         self.set_light_off()
if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
