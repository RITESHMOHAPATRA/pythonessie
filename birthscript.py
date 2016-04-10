#!/usr/bin/python2.7
from time import sleep
import sys

import sys

class ProgressBar():
    DEFAULT_BAR_LENGTH = float(65)

    def __init__(self, end, start=0):
        self.end    = end
        self.start  = start
        self._barLength = ProgressBar.DEFAULT_BAR_LENGTH

        self.setLevel(self.start)
        self._plotted = False

    def setLevel(self, level, initial=False):
        self._level = level
        if level < self.start:  self._level = self.start
        if level > self.end:    self._level = self.end

        self._ratio = float(self._level - self.start) / float(self.end - self.start)
        self._levelChars = int(self._ratio * self._barLength)

    def plotProgress(self):
        sys.stdout.write("\r  %3i%% [%s%s]" %(
            int(self._ratio * 100.0),
            '=' * int(self._levelChars),
            ' ' * int(self._barLength - self._levelChars),
        ))
        sys.stdout.flush()
        self._plotted = True

    def setAndPlot(self, level):
        oldChars = self._levelChars
        self.setLevel(level)
        if (not self._plotted) or (oldChars != self._levelChars):
            self.plotProgress()

    def __del__(self):
        sys.stdout.write("\n")


def congrats():
    print """                                                    YYYYY
    HHHHH         HHHHH                             YYY          YYYY
    HHHHH         HHHHH                  PP PPPPPP   YYY         YYY
      HHH         HHH                     PPP    PP   YYY       YYY
      HHH         HHH    AAAAA  PP PPPPPP  PP    PP    YYY     YYY
      HHH         HHH   AAAAAAA  PPP    PP PP    PP     YYY   YYY
      HHH         HHH  AA     AA  PP    PP PP    PP      YYY YYY
      HHH         HHH  AA     AA  PP    PP PPPPPPP        YYYYY
      HHHHHHHHHHHHHHH  AA     AA  PP    PP PP             YYYY
      HHHHHHHHHHHHHHH  AA     AA  PPPPPPP  PP            YYYY   -------
      HHHHHHHHHHHHHHH  AAAAAAAAA  PP       PP           YYYY    -------
      HHH         HHH  AAAAAAAAA  PP       PP          YYYY     -------
      HHH         HHH  AA     AA  PP       PP         YYYY
      HHH         HHH  AA     AA  PP       PP        YYYY
      HHH         HHH  AA     AA  PP       PP      YYYYYY
      HHH         HHH  AA     AA  PP       PP     YYYYYYY
      HHH         HHH             PP       PP    YYYYYYY
    HHHHH         HHHHH           PP       PP   YYYYYYY
    HHHHH         HHHHH           PP       PP  YYYYYYY
                                                YYYYY
    BBBBBBBBBBBBB                                YYY
    BBBBBBBBBBBBBB                                Y
     BBBB       BBB    II                                   YYY             YYY
      BB         BB    II               DDDDDDDDDDDDD       YYYY           YYYY
      BB         BB                     DDDDDDDDDDDDDD        YY            YY
      BB         BB   III  RRR RRRR        DDD      DDD      A YY          YY
      BB         BB    II   RRRR  RR       DDD      DDD     AAA YY        YY
      BB        BBB    II    RRR           DDD      DDD    AAAAA YY      YY
      BBB     BBBB     II    RR            DDD      DDD   AAAAAAA YY    YY
      BBBBBBBBBBB      II    RR            DDD      DDD  AA     AA YY  YY
      BBBBBBBBB        II    RR            DDD      DDD  AA     AA  YYYY
      BBBBBBBBBBB      II    RR            DDD      DDD  AAAAAAAAA   YYY
      BBB     BBBB    IIII  RRRR           DDD      DDD  AAAAAAAAA   YYY
      BB        BBB             HHH        DDD      DDD  AA     AA   YYY
      BB         BBB    TT     HHHH        DDD      DDD  AA     AA   YYY
      BB         BBB    TT     HH          DDD      DDD  AA     AA   YYY
      BB          BBB TTTTTT   HH          DDD      DDD  AA     AA   YYY
      BB          BBB   TT     HH          DDD      DDD              YYY
      BB          BBB   TT     HHHHHHHH  DDDDDDDDDDDDD               YYY
      BB         BBB    TT     HH     HH DDDDDDDDDDDD               YYYY
     BBBB       BBBB    TT     HH     HH                           YYYY
    BBBBBBBBBBBBBBB     TT  TT HH     HH    YYYYYYYYYYYYYYYYYYYYYYYYYY
    BBBBBBBBBBBBBB       TTTT  HH     HH    YYYYYYYYYYYYYYYYYYYYYYYY
                              HHHH   HHHH   YYYYYYYYYYYYYYYYYYYYYY
    """

if __name__ == "__main__":
    import time
    count = 5
    question = raw_input("It'your birthday? (Y/N) ")

    if question.lower() == 'yes' or question.startswith('y') or question.startswith('Y'):
        print 'OK. Loading ',
        pb = ProgressBar(count)
        curProgress = 0
        while curProgress <= count:
            pb.setAndPlot(curProgress)
            curProgress += 1
            time.sleep(.5)
        del pb
        print 'Loaded!',
        sleep(.5)
        congrats()
    else:
        print'Oh, sorry, then happy no-birthday :D'
        sleep(.5)
        print """

                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '''$$$
   "$$$'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     ""'$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$""$$$$$$'''''           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  '$$$o$$$$$$$$$'''
                        "'$$$$$$$oo $$$$$$$$$$
                                ''''$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$'''"""



