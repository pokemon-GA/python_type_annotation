#型アノテーション
from typing import List, Dict, Optional, Union, Tuple, Iterable, Final, Literal


#int型
integer: int = 100

#float型
float_numebr: float = 1.1

#string型
string: str = 'HelloWorld'

#bool型
boolean: bool = True

#any型
# any_type: any = 123

#none型
no_type: None = None

#辞書型
#Dict[keyの型, valueの型]
dictionaly: Dict[str, int] = {
    'hello': 1,
    'evening': 2
}

#配列
#List[型]
list: List[int] = [1,2,3]

#指定した型もしくはNone
str_or_none_1: Optional[str] = 'Hello'
str_or_none_2: Optional[str] = None

#タプル
#Tuple[型, 型, ...]
tuple_type: Tuple[int, str, bool] = (12, 'HelloWorld', True)

#任意のイテラブルの型確認
#イテラブル ... 繰り返し可能なオブジェクト
#辞書式は、判定できない
#*Iterableは、1つの型しか持つことができないことに注意
y: Iterable[str] = ['a', 'b', 'c']
z: Iterable[bool] = (True, True, False)


#合併型
#Union[型,　型, ...]
str_or_int_1: Union[str, int] = 'Hello'
str_or_int_2: Union[str, int] = 12
#python3.10から 型A | 型B とつなげることができる
# str_or_int_new_1: str | int = 'Hello'
# str_or_int_new_2: str | int = 'Hello'

#*関数のアノテーション
def add(a:int, b: int) -> int:
    return int(a*b)

#定数化
UNKO_CONST: Final = 'HelloWorld'

#自作の型
#Literal[整数 or 文字列] <-このリスト内の者しか受け付けない
hello: Literal['hello'] = 'hello'

#TypeGuard
#参考リンク
#https://qiita.com/simonritchie/items/f64d31324f2ed804ecc8#%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E3%81%8C%E5%AE%9A%E7%BE%A9%E3%81%99%E3%82%8Btypeguard%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6