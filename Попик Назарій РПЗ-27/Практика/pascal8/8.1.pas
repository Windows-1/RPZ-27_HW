var a,b:string;
    i:byte;
begin
    write('строка A = ');readln(a);
    write('строка B = ');readln(b);
    for i:=Length(a) downto 1 do
      while Pos(a[i],b)>0 do
        Delete(a,i,1);
    writeln('Полученная строка = ',a);
end.