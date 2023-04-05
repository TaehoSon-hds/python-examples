inputs: final: prev: with final;
{

  mypython = with python310Packages; [
    flake8
    black

    pandas
    requests
    beautifulsoup4
  ];

}
