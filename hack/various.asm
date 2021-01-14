arch 65816
lorom

;; TABLE FOR INSERTION
table "various.tbl",rtl

;; LIMIT: 14 chars
;; SPACE: $03
;;
org $3a336
   db "Found         "
   db "Received      "
   db "Learned to use"
   db "Won           "
   db "Bought        "

org 3a37c
   db "A B C D E F G H I J K L M",$02
   db "N O P Q R S T U V W X Y Z",$02
   db "a b c d e f g h i j k l m",$02
   db "n o p q r s t u v w x y z",$02
   db ". , ' : ; - … / & > % ! ?",$02
   db "0 1 2 3 4 5 6 7 8 9"
   db $00

;; NOTE: There are 32 bytes of FF