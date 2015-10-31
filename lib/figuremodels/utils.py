

def checkTypeParams(*aTypes,**kTypes):
    def deco(fn):
        def fn2(*args,**kwargs):
            # [*] 
            for val,aType in zip(args,aTypes):
                if not isinstance(val,aType):
                    raise TypeError("expected %s, got %s (%s)"\
                                            % (aType, type(val),fn.func_closure[0].cell_contents))
            # [**]
            for param,val in kwargs.items():
                if kTypes.has_key(param) and \
                        not isinstance(val,kTypes[param]):
                    raise TypeError("[%s]expected %s, got %s (%s)"\
                                            % (param,kTypes[param], type(val),fn.func_closure[0].cell_contents))
            return fn(*args,**kwargs)
        return fn2
    return deco    

def checkTypeReturned(*aTypes):
    def deco(fn):
        def fn2(*args,**kwargs):
            res = fn(*args,**kwargs)
            if isinstance(res,(list,tuple)):
                if len(aTypes)>0 and isinstance(res,aTypes[0]):
                    return res
                else:
                    resT = res
            else:
                resT = res,

            for r,aType in zip(resT,aTypes):
                if not isinstance(r,aType):
                    raise TypeError("expected %s, got %s (%s)"\
                                            % (aType, type(r),fn.func_closure[0].cell_contents))
            return res
        return fn2
    return deco    
                
if __name__ == "__main__":
    
    @checkTypeParams(int,lola = int)
    @checkTypeReturned(str,int,dict)
    def testMethod(nb,lola= 1):
        res = lola+nb
        return "%f"%res,res,{"res":res}
    
    print testMethod(9,lola=3)
    try:
        testMethod(lola="5")
    except Exception as e:
        print repr(e)

