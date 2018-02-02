#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-Rcpp
Version  : 0.12.15
Release  : 61
URL      : https://cran.r-project.org/src/contrib/Rcpp_0.12.15.tar.gz
Source0  : https://cran.r-project.org/src/contrib/Rcpp_0.12.15.tar.gz
Summary  : Seamless R and C++ Integration
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-Rcpp-lib
Requires: R-markdown
BuildRequires : R-markdown
BuildRequires : clr-R-helpers

%description
offer a seamless integration of R and C++. Many R data types and objects can be
 mapped back and forth to C++ equivalents which facilitates both writing of new
 code as well as easier integration of third-party libraries. Documentation 
 about 'Rcpp' is provided by several vignettes included in this package, via the

%package lib
Summary: lib components for the R-Rcpp package.
Group: Libraries

%description lib
lib components for the R-Rcpp package.


%prep
%setup -q -c -n Rcpp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1516471839

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1516471839
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rcpp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rcpp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library Rcpp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library Rcpp|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || : || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/Rcpp/CITATION
/usr/lib64/R/library/Rcpp/DESCRIPTION
/usr/lib64/R/library/Rcpp/INDEX
/usr/lib64/R/library/Rcpp/Meta/Rd.rds
/usr/lib64/R/library/Rcpp/Meta/features.rds
/usr/lib64/R/library/Rcpp/Meta/hsearch.rds
/usr/lib64/R/library/Rcpp/Meta/links.rds
/usr/lib64/R/library/Rcpp/Meta/nsInfo.rds
/usr/lib64/R/library/Rcpp/Meta/package.rds
/usr/lib64/R/library/Rcpp/Meta/vignette.rds
/usr/lib64/R/library/Rcpp/NAMESPACE
/usr/lib64/R/library/Rcpp/NEWS.Rd
/usr/lib64/R/library/Rcpp/R/Rcpp
/usr/lib64/R/library/Rcpp/R/Rcpp.rdb
/usr/lib64/R/library/Rcpp/R/Rcpp.rdx
/usr/lib64/R/library/Rcpp/README
/usr/lib64/R/library/Rcpp/THANKS
/usr/lib64/R/library/Rcpp/announce/ANNOUNCE-0.10.0.txt
/usr/lib64/R/library/Rcpp/announce/ANNOUNCE-0.11.0.txt
/usr/lib64/R/library/Rcpp/announce/ANNOUNCE-0.6.0.txt
/usr/lib64/R/library/Rcpp/announce/ANNOUNCE-0.7.0.txt
/usr/lib64/R/library/Rcpp/announce/ANNOUNCE-0.8.0.txt
/usr/lib64/R/library/Rcpp/announce/ANNOUNCE-0.9.0.txt
/usr/lib64/R/library/Rcpp/bib/Rcpp.bib
/usr/lib64/R/library/Rcpp/discovery/cxx0x.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-FAQ.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-FAQ.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-FAQ.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-attributes.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-attributes.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-attributes.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-extending.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-extending.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-extending.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-introduction.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-introduction.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-introduction.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-jss-2011.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-jss-2011.Rnw
/usr/lib64/R/library/Rcpp/doc/Rcpp-jss-2011.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-modules.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-modules.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-modules.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-package.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-package.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-quickref.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-quickref.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-quickref.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-sugar.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-sugar.Rmd
/usr/lib64/R/library/Rcpp/doc/Rcpp-sugar.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp-unitTests.R
/usr/lib64/R/library/Rcpp/doc/Rcpp-unitTests.Rnw
/usr/lib64/R/library/Rcpp/doc/Rcpp-unitTests.pdf
/usr/lib64/R/library/Rcpp/doc/Rcpp.bib
/usr/lib64/R/library/Rcpp/doc/index.html
/usr/lib64/R/library/Rcpp/examples/Attributes/Depends.cpp
/usr/lib64/R/library/Rcpp/examples/Attributes/Export.cpp
/usr/lib64/R/library/Rcpp/examples/Attributes/cppFunction.R
/usr/lib64/R/library/Rcpp/examples/Attributes/sourceCpp.R
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/GNUmakefile
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/buildAndRun.sh
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve10_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve10_cpp.h
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve11_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve12_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve13_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve14_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve2_c.c
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve3_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve4_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve5_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve7_c.c
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve8_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/convolve9_cpp.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/exampleRCode.r
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/loopmacro.h
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/overhead.r
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/overhead.sh
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/overhead_1.cpp
/usr/lib64/R/library/Rcpp/examples/ConvolveBenchmarks/overhead_2.c
/usr/lib64/R/library/Rcpp/examples/FastLM/benchmark.r
/usr/lib64/R/library/Rcpp/examples/FastLM/benchmarkLongley.r
/usr/lib64/R/library/Rcpp/examples/FastLM/fastLMviaArmadillo.r
/usr/lib64/R/library/Rcpp/examples/FastLM/fastLMviaGSL.r
/usr/lib64/R/library/Rcpp/examples/FastLM/lmArmadillo.R
/usr/lib64/R/library/Rcpp/examples/FastLM/lmGSL.R
/usr/lib64/R/library/Rcpp/examples/Misc/fibonacci.r
/usr/lib64/R/library/Rcpp/examples/Misc/ifelseLooped.r
/usr/lib64/R/library/Rcpp/examples/Misc/newFib.r
/usr/lib64/R/library/Rcpp/examples/Misc/piBySimulation.r
/usr/lib64/R/library/Rcpp/examples/Misc/piSugar.cpp
/usr/lib64/R/library/Rcpp/examples/OpenMP/GNUmakefile
/usr/lib64/R/library/Rcpp/examples/OpenMP/OpenMPandInline.r
/usr/lib64/R/library/Rcpp/examples/OpenMP/check.R
/usr/lib64/R/library/Rcpp/examples/OpenMP/piWithInterrupts.cpp
/usr/lib64/R/library/Rcpp/examples/RcppGibbs/RcppGibbs.R
/usr/lib64/R/library/Rcpp/examples/RcppGibbs/timeRNGs.R
/usr/lib64/R/library/Rcpp/examples/RcppInline/RObject.r
/usr/lib64/R/library/Rcpp/examples/RcppInline/RcppInlineExample.r
/usr/lib64/R/library/Rcpp/examples/RcppInline/RcppInlineWithLibsExamples.r
/usr/lib64/R/library/Rcpp/examples/RcppInline/RcppSimpleExample.r
/usr/lib64/R/library/Rcpp/examples/RcppInline/UncaughtExceptions.r
/usr/lib64/R/library/Rcpp/examples/RcppInline/external_pointer.r
/usr/lib64/R/library/Rcpp/examples/SugarPerformance/Timer.h
/usr/lib64/R/library/Rcpp/examples/SugarPerformance/Timertest.cpp
/usr/lib64/R/library/Rcpp/examples/SugarPerformance/sugarBenchmarks.R
/usr/lib64/R/library/Rcpp/examples/functionCallback/README
/usr/lib64/R/library/Rcpp/examples/functionCallback/newApiExample.r
/usr/lib64/R/library/Rcpp/examples/performance/extractors.R
/usr/lib64/R/library/Rcpp/examples/performance/performance.R
/usr/lib64/R/library/Rcpp/help/AnIndex
/usr/lib64/R/library/Rcpp/help/Rcpp.rdb
/usr/lib64/R/library/Rcpp/help/Rcpp.rdx
/usr/lib64/R/library/Rcpp/help/aliases.rds
/usr/lib64/R/library/Rcpp/help/paths.rds
/usr/lib64/R/library/Rcpp/html/00Index.html
/usr/lib64/R/library/Rcpp/html/R.css
/usr/lib64/R/library/Rcpp/include/Rcpp.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Benchmark/Timer.h
/usr/lib64/R/library/Rcpp/include/Rcpp/DataFrame.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Dimension.h
/usr/lib64/R/library/Rcpp/include/Rcpp/DottedPair.h
/usr/lib64/R/library/Rcpp/include/Rcpp/DottedPairImpl.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Environment.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Extractor.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Fast.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Formula.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Function.h
/usr/lib64/R/library/Rcpp/include/Rcpp/InputParameter.h
/usr/lib64/R/library/Rcpp/include/Rcpp/InternalFunction.h
/usr/lib64/R/library/Rcpp/include/Rcpp/InternalFunctionWithStdFunction.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Interrupt.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Language.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Module.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Na_Proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Named.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Nullable.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Pairlist.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Promise.h
/usr/lib64/R/library/Rcpp/include/Rcpp/RNGScope.h
/usr/lib64/R/library/Rcpp/include/Rcpp/RObject.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Reference.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Rmath.h
/usr/lib64/R/library/Rcpp/include/Rcpp/S4.h
/usr/lib64/R/library/Rcpp/include/Rcpp/StretchyList.h
/usr/lib64/R/library/Rcpp/include/Rcpp/String.h
/usr/lib64/R/library/Rcpp/include/Rcpp/StringTransformer.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Symbol.h
/usr/lib64/R/library/Rcpp/include/Rcpp/Vector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/WeakReference.h
/usr/lib64/R/library/Rcpp/include/Rcpp/XPtr.h
/usr/lib64/R/library/Rcpp/include/Rcpp/algo.h
/usr/lib64/R/library/Rcpp/include/Rcpp/algorithm.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/bones/Date.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/bones/Datetime.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/bones/bones.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/bones/wrap_extra_steps.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/DataFrame.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/Date.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/Datetime.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/Dimension.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/DottedPairImpl.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/Environment.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/Rcpp_eval.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/S4.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/StretchyList.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/Vector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/as.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/export.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/is.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/meat.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/module/Module.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/protection.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/api/meat/wrap.h
/usr/lib64/R/library/Rcpp/include/Rcpp/as.h
/usr/lib64/R/library/Rcpp/include/Rcpp/barrier.h
/usr/lib64/R/library/Rcpp/include/Rcpp/clone.h
/usr/lib64/R/library/Rcpp/include/Rcpp/complex.h
/usr/lib64/R/library/Rcpp/include/Rcpp/config.h
/usr/lib64/R/library/Rcpp/include/Rcpp/date_datetime/Date.h
/usr/lib64/R/library/Rcpp/include/Rcpp/date_datetime/Datetime.h
/usr/lib64/R/library/Rcpp/include/Rcpp/date_datetime/date_datetime.h
/usr/lib64/R/library/Rcpp/include/Rcpp/date_datetime/newDateVector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/date_datetime/newDatetimeVector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/date_datetime/oldDateVector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/date_datetime/oldDatetimeVector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/exceptions.h
/usr/lib64/R/library/Rcpp/include/Rcpp/exceptions/cpp11/exceptions.h
/usr/lib64/R/library/Rcpp/include/Rcpp/exceptions/cpp98/exceptions.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/DataFrame_generated.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/DottedPair__ctors.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/Function__operator.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/InternalFunctionWithStdFunction_call.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/InternalFunction__ctors.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/Language__ctors.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/Pairlist__ctors.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/Vector__create.h
/usr/lib64/R/library/Rcpp/include/Rcpp/generated/grow__pairlist.h
/usr/lib64/R/library/Rcpp/include/Rcpp/grow.h
/usr/lib64/R/library/Rcpp/include/Rcpp/hash/IndexHash.h
/usr/lib64/R/library/Rcpp/include/Rcpp/hash/SelfHash.h
/usr/lib64/R/library/Rcpp/include/Rcpp/hash/hash.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/Exporter.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/GreedyVector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/ListInitialization.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/NAComparator.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/NAEquals.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/Proxy_Iterator.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/SEXP_Iterator.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/caster.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/converter.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/export.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/na.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/r_coerce.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/r_vector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/wrap.h
/usr/lib64/R/library/Rcpp/include/Rcpp/internal/wrap_end.h
/usr/lib64/R/library/Rcpp/include/Rcpp/iostream/Rstreambuf.h
/usr/lib64/R/library/Rcpp/include/Rcpp/is.h
/usr/lib64/R/library/Rcpp/include/Rcpp/lang.h
/usr/lib64/R/library/Rcpp/include/Rcpp/longlong.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/cat.hpp
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/config.hpp
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/debug.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/dispatch.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/interface.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/macros.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/module.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/traits.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/unroll.h
/usr/lib64/R/library/Rcpp/include/Rcpp/macros/xp.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/CppFunction.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_Add_Property.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_Field.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_Property.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_Constructor.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_CppFunction.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_CppMethod.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_Factory.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_Pointer_CppMethod.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_Pointer_method.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_class_constructor.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_class_factory.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_class_signature.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_ctor_signature.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_function.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_get_signature.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/Module_generated_method.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/class.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/class_Base.h
/usr/lib64/R/library/Rcpp/include/Rcpp/module/get_return_type.h
/usr/lib64/R/library/Rcpp/include/Rcpp/platform/compiler.h
/usr/lib64/R/library/Rcpp/include/Rcpp/platform/solaris.h
/usr/lib64/R/library/Rcpp/include/Rcpp/print.h
/usr/lib64/R/library/Rcpp/include/Rcpp/protection/Armor.h
/usr/lib64/R/library/Rcpp/include/Rcpp/protection/Shelter.h
/usr/lib64/R/library/Rcpp/include/Rcpp/protection/Shield.h
/usr/lib64/R/library/Rcpp/include/Rcpp/protection/protection.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/AttributeProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/Binding.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/DottedPairProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/FieldProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/GenericProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/NamesProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/ProtectedProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/RObjectMethods.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/SlotProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/TagProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/proxy/proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/r/headers.h
/usr/lib64/R/library/Rcpp/include/Rcpp/r_cast.h
/usr/lib64/R/library/Rcpp/include/Rcpp/routines.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sprintf.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/beta.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/binom.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/cauchy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/chisq.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/dpq/dpq.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/dpq/macros.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/exp.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/f.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/gamma.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/geom.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/hyper.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/lnorm.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/logis.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/nbeta.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/nbinom.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/nbinom_mu.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/nchisq.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/nf.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/norm.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/nt.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/pois.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/random.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rbeta.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rbinom.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rcauchy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rchisq.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rexp.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rf.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rgamma.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rgeom.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rhyper.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rlnorm.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rlogis.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rnbinom.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rnbinom_mu.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rnchisq.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rnorm.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rpois.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rsignrank.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rt.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/runif.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rweibull.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/random/rwilcox.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/stats.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/t.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/unif.h
/usr/lib64/R/library/Rcpp/include/Rcpp/stats/weibull.h
/usr/lib64/R/library/Rcpp/include/Rcpp/storage/NoProtectStorage.h
/usr/lib64/R/library/Rcpp/include/Rcpp/storage/PreserveStorage.h
/usr/lib64/R/library/Rcpp/include/Rcpp/storage/storage.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/Range.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/block/SugarBlock_1.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/block/SugarBlock_2.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/block/SugarBlock_3.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/block/SugarMath.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/block/Vectorized_Math.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/block/block.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/Lazy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/all.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/any.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/cbind.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/clamp.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/complex.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/cummax.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/cummin.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/cumprod.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/cumsum.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/diff.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/duplicated.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/functions.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/head.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/ifelse.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/is_finite.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/is_infinite.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/is_na.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/is_nan.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/lapply.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/mapply.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/mapply/mapply_2.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/mapply/mapply_3.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/match.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/math.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/max.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/mean.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/median.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/min.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/na_omit.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/pmax.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/pmin.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/pow.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/range.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/rep.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/rep_each.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/rep_len.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/rev.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/rowSums.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/sample.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/sapply.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/sd.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/self_match.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/seq_along.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/setdiff.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/sign.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/strings/collapse.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/strings/strings.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/strings/trimws.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/sum.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/table.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/tail.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/unique.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/var.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/which_max.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/functions/which_min.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/logical/SingleLogicalResult.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/logical/and.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/logical/can_have_na.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/logical/is.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/logical/logical.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/logical/not.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/logical/or.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/as_vector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/col.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/diag.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/lower_tri.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/matrix_functions.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/outer.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/row.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/tools.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/matrix/upper_tri.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/nona/nona.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/Comparator.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/Comparator_With_One_Value.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/divides.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/logical_operators__Vector__Vector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/logical_operators__Vector__primitive.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/minus.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/not.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/operators.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/plus.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/r_binary_op.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/times.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/operators/unary_minus.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/sets.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/sugar.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/sugar_forward.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/tools/iterator.h
/usr/lib64/R/library/Rcpp/include/Rcpp/sugar/undoRmath.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/char_type.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/enable_if.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/expands_to_logical.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/get_na.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/has_iterator.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/has_na.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/if_.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/init_type.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/integral_constant.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_arithmetic.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_bool.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_const.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_convertible.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_eigen_base.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_finite.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_infinite.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_module_object.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_na.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_nan.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_pointer.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_primitive.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_reference.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_sugar_expression.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_trivial.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/is_wide_string.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/longlong.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/matrix_interface.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/module_wrap_traits.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/named_object.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/num2type.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/one_type.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/r_sexptype_traits.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/r_type_traits.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/remove_const.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/remove_const_and_reference.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/remove_reference.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/result_of.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/same_type.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/storage_type.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/traits.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/un_pointer.h
/usr/lib64/R/library/Rcpp/include/Rcpp/traits/wrap_type_traits.h
/usr/lib64/R/library/Rcpp/include/Rcpp/utils/tinyformat.h
/usr/lib64/R/library/Rcpp/include/Rcpp/utils/tinyformat/tinyformat.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/00_forward_Vector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/00_forward_proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/ChildVector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/DimNameProxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/LazyVector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/ListOf.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/Matrix.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/MatrixBase.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/MatrixColumn.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/MatrixRow.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/RangeIndexer.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/SubMatrix.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/Subsetter.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/Vector.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/VectorBase.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/const_generic_proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/const_string_proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/converter.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/generic_proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/instantiation.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/no_init.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/string_proxy.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/swap.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/traits.h
/usr/lib64/R/library/Rcpp/include/Rcpp/vector/vector_from_string.h
/usr/lib64/R/library/Rcpp/include/RcppCommon.h
/usr/lib64/R/library/Rcpp/include/doxygen/Examples.h
/usr/lib64/R/library/Rcpp/libs/symbols.rds
/usr/lib64/R/library/Rcpp/prompt/module.Rd
/usr/lib64/R/library/Rcpp/skeleton/Num.cpp
/usr/lib64/R/library/Rcpp/skeleton/Rcpp_modules_examples.Rd
/usr/lib64/R/library/Rcpp/skeleton/manual-page-stub.Rd
/usr/lib64/R/library/Rcpp/skeleton/rcpp_hello_world.R
/usr/lib64/R/library/Rcpp/skeleton/rcpp_hello_world.Rd
/usr/lib64/R/library/Rcpp/skeleton/rcpp_hello_world.cpp
/usr/lib64/R/library/Rcpp/skeleton/rcpp_hello_world.h
/usr/lib64/R/library/Rcpp/skeleton/rcpp_hello_world_attributes.cpp
/usr/lib64/R/library/Rcpp/skeleton/rcpp_module.cpp
/usr/lib64/R/library/Rcpp/skeleton/stdVector.cpp
/usr/lib64/R/library/Rcpp/skeleton/zzz.R
/usr/lib64/R/library/Rcpp/unitTests/bin/amd64/r-cran-testrcpppackage_0.1.0-1_amd64.deb
/usr/lib64/R/library/Rcpp/unitTests/bin/i386/r-cran-testrcpppackage_0.1.0-1_i386.deb
/usr/lib64/R/library/Rcpp/unitTests/cpp/DataFrame.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/Environment.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/Function.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/InternalFunction.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/InternalFunctionCPP11.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/ListOf.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/Matrix.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/Module.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/RObject.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/Reference.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/S4.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/String.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/Subset.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/Vector.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/VectorOld.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/XPtr.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/algorithm.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/as.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/attributes.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/attributes.hpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/dates.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/dispatch.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/exceptions.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/language.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/misc.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/modref.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/na.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/rmath.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/stack.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/stats.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/sugar.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/support.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/table.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/wrap.cpp
/usr/lib64/R/library/Rcpp/unitTests/cpp/wstring.cpp
/usr/lib64/R/library/Rcpp/unitTests/runTests.R
/usr/lib64/R/library/Rcpp/unitTests/runit.DataFrame.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Date.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Function.R
/usr/lib64/R/library/Rcpp/unitTests/runit.InternalFunction.R
/usr/lib64/R/library/Rcpp/unitTests/runit.InternalFunctionCPP11.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Language.R
/usr/lib64/R/library/Rcpp/unitTests/runit.ListOf.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Matrix.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Module.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Module.client.package.R
/usr/lib64/R/library/Rcpp/unitTests/runit.RObject.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Rcpp.package.skeleton.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Reference.R
/usr/lib64/R/library/Rcpp/unitTests/runit.S4.R
/usr/lib64/R/library/Rcpp/unitTests/runit.String.R
/usr/lib64/R/library/Rcpp/unitTests/runit.Vector.R
/usr/lib64/R/library/Rcpp/unitTests/runit.VectorOld.R
/usr/lib64/R/library/Rcpp/unitTests/runit.XPTr.R
/usr/lib64/R/library/Rcpp/unitTests/runit.algorithm.R
/usr/lib64/R/library/Rcpp/unitTests/runit.as.R
/usr/lib64/R/library/Rcpp/unitTests/runit.attributes.R
/usr/lib64/R/library/Rcpp/unitTests/runit.binary.package.R
/usr/lib64/R/library/Rcpp/unitTests/runit.client.package.R
/usr/lib64/R/library/Rcpp/unitTests/runit.dispatch.R
/usr/lib64/R/library/Rcpp/unitTests/runit.environments.R
/usr/lib64/R/library/Rcpp/unitTests/runit.exceptions.R
/usr/lib64/R/library/Rcpp/unitTests/runit.misc.R
/usr/lib64/R/library/Rcpp/unitTests/runit.modref.R
/usr/lib64/R/library/Rcpp/unitTests/runit.na.R
/usr/lib64/R/library/Rcpp/unitTests/runit.quickanddirty.R
/usr/lib64/R/library/Rcpp/unitTests/runit.rmath.R
/usr/lib64/R/library/Rcpp/unitTests/runit.stack.R
/usr/lib64/R/library/Rcpp/unitTests/runit.stats.R
/usr/lib64/R/library/Rcpp/unitTests/runit.subset.R
/usr/lib64/R/library/Rcpp/unitTests/runit.sugar.R
/usr/lib64/R/library/Rcpp/unitTests/runit.sugar.var.R
/usr/lib64/R/library/Rcpp/unitTests/runit.support.R
/usr/lib64/R/library/Rcpp/unitTests/runit.system.R
/usr/lib64/R/library/Rcpp/unitTests/runit.table.R
/usr/lib64/R/library/Rcpp/unitTests/runit.wrap.R
/usr/lib64/R/library/Rcpp/unitTests/runit.wstring.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/DESCRIPTION
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/NAMESPACE
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/R/load.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/R/rcpp_hello_world.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/man/Rcpp_class_examples.Rd
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/man/rcpp_hello_world.Rd
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/man/testRcppClass-package.Rd
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/src/Num.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/src/init.c
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/src/rcpp_hello_world.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/src/rcpp_hello_world.h
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/src/rcpp_module.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/src/stdVector.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppClass/tests/classes.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/DESCRIPTION
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/NAMESPACE
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/R/rcpp_hello_world.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/R/zzz.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/man/Rcpp_modules_examples.Rd
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/man/rcpp_hello_world.Rd
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/man/testRcppModule-package.Rd
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/src/Num.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/src/init.c
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/src/rcpp_hello_world.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/src/rcpp_hello_world.h
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/src/rcpp_module.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/src/stdVector.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppModule/tests/modules.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppPackage/DESCRIPTION
/usr/lib64/R/library/Rcpp/unitTests/testRcppPackage/NAMESPACE
/usr/lib64/R/library/Rcpp/unitTests/testRcppPackage/R/rcpp_hello_world.R
/usr/lib64/R/library/Rcpp/unitTests/testRcppPackage/man/testRcppPackage-package.Rd
/usr/lib64/R/library/Rcpp/unitTests/testRcppPackage/src/rcpp_hello_world.cpp
/usr/lib64/R/library/Rcpp/unitTests/testRcppPackage/src/rcpp_hello_world.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/Rcpp/libs/Rcpp.so
/usr/lib64/R/library/Rcpp/libs/Rcpp.so.avx2
/usr/lib64/R/library/Rcpp/libs/Rcpp.so.avx512
