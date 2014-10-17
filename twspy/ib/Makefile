SRC := ./src/IBJts/source/JavaClient/com/ib/client
OBJ := $(addsuffix .py, $(basename $(notdir $(wildcard $(SRC)/*.java))))

all:
	$(MAKE) -C src
	$(MAKE) obj

obj: $(OBJ)

$(OBJ): %.py: $(SRC)/%.java cfg/%.py cfg/__init__.py
	PYTHONPATH= j2py -c cfg -d cfg $< $@

clean:
	rm -f $(OBJ)
