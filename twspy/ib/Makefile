JTS := ./src/IBJts
SRC := $(JTS)/source/JavaClient/com/ib/client
OBJ := $(addsuffix .py, $(basename $(notdir $(wildcard $(SRC)/*.java))))

all:
	$(MAKE) -C src
	$(MAKE) obj

obj: $(OBJ) __init__.py

$(OBJ): %.py: $(SRC)/%.java cfg/%.py cfg/__init__.py
	PYTHONPATH= j2py -c cfg -d cfg $< $@

__init__.py: $(JTS)/.version
	echo "__version__ = '`cat $(JTS)/.version`'" > __init__.py

clean:
	rm -f $(OBJ) __init__.py
