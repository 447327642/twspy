JAR := twsapi_macunix.971.01.jar
URL := http://interactivebrokers.github.io/downloads/$(JAR)

all: $(JAR) IBJts

$(JAR):
	wget $(URL)
	touch $(JAR)

IBJts: $(JAR)
	rm -rf IBJts
	jar -xf $(JAR)
	find IBJts -exec touch {} \;

clean:
	rm -rf IBJts *.jar
