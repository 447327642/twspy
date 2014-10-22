VER := 971.01
JAR := twsapi_macunix.$(VER).jar
URL := http://interactivebrokers.github.io/downloads/$(JAR)

all: $(JAR) IBJts

$(JAR):
	wget $(URL)
	touch $(JAR)

IBJts: $(JAR)
	rm -rf IBJts
	jar -xf $(JAR)
	echo "$(VER)" > IBJts/.version
	find IBJts -exec touch {} \;

clean:
	rm -rf IBJts *.jar
