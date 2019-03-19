#Compiler and Linker
CC	:= gcc

#The Target Binary Program
TARGET	  := heart_rate

#The Directories, Source, Includes, Objects, Binary and Resources
SRCDIR    := src
INCDIR    := inc
BUILDDIR  := obj
TARGETDIR := bin
LIBDIR	  := lib
SRCEXT    := c
DEPEXT    := d
OBJEXT    := o

#Flags, Libraries and Includes
CFLAGS := -g -O2 -Wall -Wextra -Isrc -rdynamic -DNDEBUG $(OPTFLAGS)
CFLAGS += -Wno-unused-parameter -Wno-unused-command-line-argument
LIB    := 
INC    := -I$(INCDIR) -I/usr/local/include
INCDEP := -I$(INCDIR)

#---------------------------------------------------------------------------------
#DO NOT EDIT BELOW THIS LINE
#---------------------------------------------------------------------------------
SOURCES	 := $(shell find $(SRCDIR) -type f -name *.$(SRCEXT))
OBJECTS	 := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:.$(SRCEXT)=.$(OBJEXT)))

#Default Make
all: lib

#Remake
remake: cleaner all

#Make the Directories
directories:
	@mkdir -p $(TARGETDIR)
	@mkdir -p $(BUILDDIR)
	@mkdir -p $(LIBDIR)

#Clean only Objecst
clean:
	@$(RM) -rf $(BUILDDIR) $(TARGETDIR) $(LIBDIR)

#Full Clean, Objects and Binaries
cleaner: clean
	@$(RM) -rf $(TARGETDIR)

run:
	make clean
	make directories
	make executable
	clear
	./bin/$(TARGET)

lib: directories
	$(CC) -shared -o $(LIBDIR)/$(TARGET).so -fPIC $(SOURCES)

#Pull in dependency info for *existing* .o files
-include $(OBJECTS:.$(OBJEXT)=.$(DEPEXT))

#Link
executable: $(OBJECTS)
		$(CC) -o $(TARGETDIR)/$(TARGET)  $^ $(LIB)

#Compile
$(BUILDDIR)/%.$(OBJEXT): $(SRCDIR)/%.$(SRCEXT)
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INC) -c -o $@ $<
	@$(CC) $(CFLAGS) $(INCDEP) -MM $(SRCDIR)/$*.$(SRCEXT) > $(BUILDDIR)/$*.$(DEPEXT)
	@cp -f $(BUILDDIR)/$*.$(DEPEXT) $(BUILDDIR)/$*.$(DEPEXT).tmp
	@sed -e 's|.*:|$(BUILDDIR)/$*.$(OBJEXT):|' < $(BUILDDIR)/$*.$(DEPEXT).tmp > $(BUILDDIR)/$*.$(DEPEXT)
	@sed -e 's/.*://' -e 's/\\$$//' < $(BUILDDIR)/$*.$(DEPEXT).tmp | fmt -1 | sed -e 's/^ *//' -e 's/$$/:/' >> $(BUILDDIR)/$*.$(DEPEXT)
	@rm -f $(BUILDDIR)/$*.$(DEPEXT).tmp

#Non-File Targets
.PHONY: all remake clean cleaner resources run lib executable