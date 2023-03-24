inputs: final: prev: with final;
{

  mypython = python310.withPackages (p: with p; [
    numpy
    pandas
    matplotlib
    scikit-learn
    jupyterlab
  ]);

}
