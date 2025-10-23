{
  description = "A basic Python development environment";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        pythonPackages = pkgs.python3Packages;
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            python3
            pythonPackages.pip
          ];
          shellHook = ''
            echo "Python development environment"
            python --version
            if [ ! -d .venv ]; then
              python -m venv .venv
            fi
            export VIRTUAL_ENV_DISABLE_PROMPT=1
            source .venv/bin/activate
          '';
        };
      });
}
